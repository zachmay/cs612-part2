# Using Genetic Algorithms for Generating Test Cases

This project aimed to reproduce the techniques described in the paper "Test-Data Generation
Using Genetic Algorithms" by Pargas, et al. [1]

To guide this genetic algorithm (GA), we analyze the structure of a C program and generate a tree of
control dependencies. Paths from the root of the tree (i.e., the entry point of the program) represent
execution paths in the program. The GA judges a set of inputs based on how well that input
covers the sites in the program along that path.

The project uses several Python libraries and depends upon Clang and LLVM for program analysis and coverage
instrumentation and reporting.

## Program Analysis

Program analysis was completed using several scripts available in this repository, although the process
is not fully automated.

Importantly, I chose to represent the structure of the program in terms of basic blocks, i.e., regions of code
such that:
    - Control flow can only enter via the first instruction in the block, and
    - Control flow can only exit via the last instruction in the block.

Using the script `bin/dump-cfg`, you can get an output of the basic blocks in a C source file. This output shows
which basic blocks can be successors or predecessors of which other blocks and, from this, we can derive the
program's control flow graph (CFG).

From there, the Python script `cdg.py` can be edited and the CFG defined by changing the contents of the 
`edges` list. Pairs in this list represent edges in the CFG, a directed graph. Manually adding an entry node
with an edge to the first basic block and an exit node with edge from the last basic block makes the result
a bit easier to use.

This script makes use of the Python library `networkx` [2] for dealing with graphs. The `dependencies` function
uses that package's `immediate_dominators()` function to compute the immediate forward dominators of each
node in the CFG. From there, it computes for all nodes *n* and *m* in the CFG whether there exists a path
from `n` to `m` that does not include the immediate forward dominator of *m*. If so, *m* is *control dependent*
on `n`. The control dependence graph (CDG), consists of all such edges (*m*, *n*).

This technique was found in the lecture slides at [3].

One limitation of this technique is that it includes redundant edges. E.g., when (*m*, *n*) and (*n*, *o*), this
result also includes an edge for (*m*, *o*). I tried implementing a transitive reduction algorithm, but that
did not seem to eliminate the redundant edges, so the implementation may not be correct.

## Coverage

The script `bin/instrument` will take the name of a C source file (without the `.c` extension) and compile it
with Clang, enabling test coverage. This generates a binary (suffixed with `-instr` for consistency) and a 
`.gcno` file that describes the coverage information that the binary will collect.

When the instrumented executable runs, a `.gcda` file is generated that includes the collected coverage data.
Using the `llvm-cov` tool, we can generate basic block coverage via:

```
llvm-cov gcov -a program.gcno
```

This results in a `.c.gcov` file shows how often a given basic block was executed, displaying `$$$$$` when a block
was never executed.

## Genetic Algorithms

A series of Python scripts in the `src/` folder were used to execute the GA experiments, employing
the DEAP library [4].

A breakdown of the purpose of each file follows.

### `Experiment.py`

This is a base class that controls running a GA using the `eaSimple` algorithm, which performs the simplest
type of genetic algorithm:

- An initial population of individuals is generated.
    - In this project, an individual is a set of inputs for a particular program.
- The fitness of each of these individuals is computed.
    - The fitness of an input is how deep into a control dependency path it takes the program.
- The fittest individuals are selected to move on to the next generation.
- Based on certain probability parameters, individuals are mutated or mated with another individual and the resulting
  individuals are added to the population.
    - Mutation is implemented as changing one of the numeric inputs to another random number.
    - Mating is performed by splicing the input at a random point and taking half from one parent and the rest
      from the other.

In this project, we run an experiment by performing an isolated GA experiment for each path in the CDG. We did not
implement the timeout technique of Pargas, et al., nor a means of stopping the experiment when an individual was 
found that fully exercises a CDG path.

### `Runner.py`

Each `Experiment` object takes a `Runner` object that is responsible for taking an input and running the
instrumented binary with it in order to discover its fitness. 

The `Runner` class is responsible for taking a set of inputs, running the program with those inputs in a
subprocess, calling the `llvm-cov` tool, and then reading in the `.c.gcov` file. This file and the `.gcda` 
file are cleaned up between runs to reset coverage data.

`Runner` also provides some methods for determining the fitness of an input based on the current run.
Given a mapping from basic block identifier to a line number in the `.c.gcov` file, we can determine
if a basic block is covered in a given run, and the fitness of an input is simply the number of 
covered basic blocks found in the path before we reach an uncovered block (see the `pathCoverageFitness()`
method).

### Individual Experiment Classes

The `Experiment` class must be extended for each individual program you want to work with. For example,
`Tritype.py` defines an `Experiment` subclass for dealing with the `tritype.c` program. 

The CDG paths and line-mapping for determining block coverage are defined, and constraints on the possibly
random inputs are given. Additionally, a method must be provided for generating a random individual and
population, since these may vary based on the nature of the program being tested.

`Tritype.py` also includes a `main()` function for firing off the experiment on the command line.

## Python Setup

The project was built using Python 2.7.10, and uses a
[Set up virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/#virtualenvironments-ref)

With `pip` and `virtualenv` installed, create a virtual environment in the current directory called `virt` and
enable it.

```
$ virtualenv virt
$ source virt/bin/activate
```

Now, use the virtual environment's version of `pip` to intall the package dependencies:

```
$ virt/bin/pip install -r dependencies.txt
```

## LLVM

I had to build Clang and LLVM from source and some files still reference my local paths and may need to be updated.

## Running the Tritype Experiment

From `experiments/tritype`:

- `../bin/instrument tritype` to build the instrumented binary.
- `python ../../src/Tritype.py`

The `main()` function in `Tritype.py` will collect the inputs it finds and run them all without
resetting the coverage statistics in between, so you can look at how well the generated set of inputs


## Future Work

By the end of the term, I was still having issues achieving satisfactory coverage using my implementation.
As Pargas, et al., describe, very simple programs (e.g., `experiments/test/test.c`) achieve 100% coverage,
often in the first generation of the GA population. However, even with 200 generations, certain CDG 
paths for `tritype.c` would never reach fitness above 1.0 (meaning, the only ever covered the program
entry point), e.g., the path ("B29", "B17", "B15", "B1"), where the following conditional short-circuits
after the second possibility:

```
if ( i+j <= k  || j+k <= i  || i+k < j) 
```

The input (5, 2, 1) executes that path at least up to "B15", although running that input against this path
results in a fitness of 1.0, so there is almost certainly a bug somewhere or an error was made when manually
setting up the coverage information for the Python scripts.

Further automating program analysis would make this technique far more useful. One issue is that the LLVM tools
I found did not seem to work well together. Basic block coverage does not use the same identifiers that are used
in the CFG dump, so tying those together would be error prone.

A great deal of time was spent trying to write LLVM plug-ins to generate coverage instrumentation and CFG
analysis that referred to the same unique identifiers, but my inexperience with LLVM led to this being an
unfruitful path. Had this been successful, a lot of hacks in the Python/GA side of the project would not
have been necessary, e.g., manually mapping basic blocks to specific lines in the coverage reporting file.

I had hoped to move beyond simply replicating Pargas's work, which is limited to programs with only a single
source file and, within that source file, only a single `main()` function. The slides [3] describe some techniques
for dealing with this, but it would have been difficult to implement from scratch.

One consideration that I think seriously limits the usefulness of this technique is the amount of program-specific
knowledge that would be required to engineer a useful GA search of its input space.

For example, a relatively simple program like a utility for decompressing compressed archive files would seemingly
require as an input an actual compressed archive. The space of possible files, even fixing the maximum size,
would be enormous, and devising techniques for constraining that space would require an immense amount of knowledge
specific to the program and the file format(s) involved.

Additionally, most interesting problems would require a host of specific knowledge to set up environments
where executions could be performed in reliable, consistent ways. For example, any network-based program would require
any number of specific system settings, mock servers, etc., to execute consistently.

In the end, I think this technique is perhaps most useful for generating test cases for isolated units of code, e.g.,
an individual function, where the input space is likely to be more constrained and the dependencies of that unit
of code can be strictly controlled. However, in those cases, it seems that techniques like test-driven development,
where unit tests are written before or concurrently with code, would produce more appropriate test cases. However, I 
have no data to back up that assertion and it still leaves us without a technique for automated test case generation
for higher-level integration tests.

### Works Cited

[1] "Test-Data Generation Using Genetic Algorithms". Pargas, Roy P., et al. Journal of Software Testing,
Verification, and Reliability. 1999.

[2] "NetworkX: High-Productivity Software for Complex Networks". (https://networkx.github.io/)

[3] "Lecture 15: Control Dependence Graphs". Anderson, Kenneth M. (https://www.cs.colorado.edu/~kena/classes/5828/s00/lectures/lecture15.pdf)

[4] "DEAP Evolutionary Computation Framework". (http://deap.readthedocs.io/en/master/)

