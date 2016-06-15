# This is an annotated version of the example at (https://github.com/deap/deap)

import random
from deap import creator, base, tools, algorithms

# Create a fitness class/function that attempts to maximize ... something.
# Arguments:
# - The name of the class; will be available as a property of `creator`
# - The base class; in this case, DEAP's base `Fitness` class
# - Additional parameters (e.g., `weights`) get passed on on to the class. In this case,
#   this 1-tuple containing a positive weight means that `FitnessMax` will be a single-objective
#   fitness function where the fitness is maximized.
creator.create("FitnessMax", base.Fitness, weights=(1.0,))

# Create a class representing an individual in the population.
# Arguments:
# - The name of the class; will be available as a property of `creator`
# - The base class; in this case, Python's built-in `list`
# - fitness: the fitness class to use to determine an individual's fitness.
creator.create("Individual", list, fitness=creator.FitnessMax)

# `Toolbox` objects contain and manage the machinery of running the GA. We will register
# components of the GA so that they are available when we start things up. It's sort of
# like a dependency injection container for the GA framework.
toolbox = base.Toolbox()

# Register `attr_bool`: This makes available in the toolbox a function that will generate
# a random boolean (0 or 1) via `toolbox.attr_bool()`
#
# `register()` sort of does partial function application. If we register:
# 
# `toolbox.register("f", random.randint, 0)`
#
# Then the toolbox will have a function `f` such that `toolbox.f(10)` will return a random
# number between 0 and 10.
toolbox.register("attr_bool", random.randint, 0, 1)

# Register `individual`: a function to generate an individual (of the type defined above).
#
# `tools.initRepeat` takes a container type (in this case, `Individual`, a subclass of `list`), 
# a function that will be repeatedly called to generate values to put into the container, and 
# a number of elements to generate.
#
# In this case, we generate `Individual`s by creating a vector of 100 random booleans.
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, n=10)

# Register `population`, a function to generate an entire population of individuals. 
#
# Here we use the built-in `list` as a container and generate individuals using the `individual`
# function we just registered. Since we don't specify `n`, we'll need to pass that in when we
# actually construct our population.
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Define an evaluation function. This just sums the number of 1-bits in the individual vector.
def evalOneMax(individual):
    return sum(individual), 

# Register `evaluate`, the function we will use to evaluate individuals, as defined above.
toolbox.register("evaluate", evalOneMax)

# Register `mate`, the method we will use to combine two individuals into a new individual.
#
# `cxTwoPoint` executes a two-point crossover. Modifies the individuals in place, but also returns
# the two new individuals as a 2-tuple.
toolbox.register("mate", tools.cxTwoPoint)

# Register `mutate`, the method we will use to mutate individuals in the population.
#
# `mutFlipBit` assumes that the individual implements Python's sequence interface and that the
# elements of that sequence behave nicely with Python's `not` operator. `indpb` is the change that
# any given attribute is flipped.
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)

# Register `select`, the method we will use to select which individuals in the population will
# be carried over to the next round.
#
# `selTournament` selects using a weighted random tournament algorithm where `tournsize` is the number
# of individuals that participate in a given round of the tournament.
toolbox.register("select", tools.selTournament, tournsize=3)

# Now we generate the initial population.
population = toolbox.population(n=10)

# Set the number of generations we want to simulate.
NGEN=20

# Define a debug function for the toolbox.
def printPop(pop, label=""):
  print label + " === Population: " + str(len(pop))
  for ind in pop:
    print ind.fitness, ind

toolbox.register("printPop", printPop)

toolbox.printPop(population, "ORIGINAL")

# Now we execute the GA, over `NGEN` generations.
# 
# In this experiment, we use the `varAnd` algorithm to take one generation to the next.
# `varAnd` is so-called because it only performs variance (mating and mutation):
# - The parent population is cloned first so that mating and mutation are not in-place
#   on the original population (it still exists independently)
# - Mating is performed without respect to individual fitness. Individual x and x+1 are mated
#   with probability `cxpb` using the toolbox's `mate` function.
# - After mating, each resulting individual undergoes mutation with probability `mutpb`.
# - Addtionally, each individual's fitness value is invalidated (set to `()`)
for gen in range(NGEN):

  # Generate the offspring of the current generation.
  offspring = algorithms.varAnd(population, toolbox, cxpb=0.5, mutpb=0.1)

  # Manually recompute the fitness of each individual (since `varAnd` doesn't care)
  fits = toolbox.map(toolbox.evaluate, offspring)
  for fit, ind in zip(fits, offspring):
      ind.fitness.values = fit

  # Run the selection process to rank population. Fitter individuals will tend to be on top.
  population = toolbox.select(offspring, k=len(population))

  toolbox.printPop(population, "GENERATION " + str(gen + 1))

# `selBest` lets us 
best = tools.selBest(population, k=3)

toolbox.printPop(best, "BEST")
