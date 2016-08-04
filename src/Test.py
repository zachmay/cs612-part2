from Experiment import Experiment
from Runner import Runner

import random
from deap import creator, tools

class Test (Experiment):
    def __init__(self, runner):
        Experiment.__init__(self, runner)

        runner.paths = \
            [ [ 1 ]
            , [ 2, 3, 4 ]
            , [ 2, 3, 5 ]
            , [ 6 ]
            ]

        runner.lineMap = \
            { 1: 16
            , 2: 17
            , 3: 26
            , 4: 21
            , 5: 23
            , 6: 30
            }

        self.minInput = -1000
        self.maxInput = 1000

    def individual(self):
        return tools.initRepeat(creator.Individual, lambda: random.randint(self.minInput, self.maxInput), 3)

    def population(self, n):
        return tools.initRepeat(list, self.toolbox.individual, n)

def main():
    workPath = '.'
    binaryName = 'test'
    coverageToolPath = '/Users/zmay/Projects/clang-dev/build/bin/llvm-cov'
    runner = Runner(workPath, binaryName, coverageToolPath)
    t = Test(runner)
    t.runAll()

if __name__ == "__main__":
    main()

# ([1], [-495, 99, -288], deap.creator.FitnessMax((0.0,)))
# ([2, 3, 4], [899, 402, -478], deap.creator.FitnessMax((1.0,)))
# ([2, 3, 5], [469, 132, -551], deap.creator.FitnessMax((1.0,)))
# ([6], [-224, -986, 189], deap.creator.FitnessMax((0.0,)))
