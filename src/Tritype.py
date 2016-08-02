from Experiment import Experiment
from Runner import Runner

import random
from deap import creator, tools

class Tritype (Experiment):
    def __init__(self, runner):
        Experiment.__init__(self, runner)

        runner.paths = \
            [ [ 1 ]
            , [ 2, 3, 4 ]
            , [ 2, 3, 5 ]
            , [ 6 ]
            ]

        runner.lineMap = \
            { 29: 46
            , 28: 47
            , 27: 49
            , 26: 52
            , 25: 57
            , 24: 59
            , 23: 61
            , 22: 63
            , 21: 65
            , 20: 67
            , 19: 70
            , 18: 79
            , 17: 80
            , 16: 81
            , 15: 83
            , 14: 86
            , 13: 88
            , 12: 96
            , 11: 98
            , 10: 100
            , 9: 101
            , 8: 103
            , 7: 105
            , 6: 106
            , 5: 108
            , 4: 110
            , 3: 111
            , 2: 113
            , 1: 116
            , 0: 122
            }

        self.minInput = -1000
        self.maxInput = 1000

    def individual(self):
        return tools.initRepeat(creator.Individual, lambda: random.randint(self.minInput, self.maxInput), 3)

    def population(self, n):
        return tools.initRepeat(list, self.toolbox.individual, n)

def main():
    workPath = '../experiments/tritype'
    binaryName = 'tritype'
    coverageToolPath = '/Users/zmay/Projects/clang-dev/build/bin/llvm-cov'
    runner = Runner(workPath, binaryName, coverageToolPath)
    t = Test(runner)
    t.runAll()

if __name__ == "__main__":
    main()

