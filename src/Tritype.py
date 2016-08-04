from Experiment import Experiment
from Runner import Runner

import random
from deap import creator, tools

class Tritype (Experiment):
    def __init__(self, runner):
        Experiment.__init__(self, runner)

        runner.paths = \
            [ ["B29", "B17", "B15", "B1"] ]

#            [ ["B29", "B16", "B15", "B1"]
#            , ["B29", "B17", "B15", "B1"]
#            , ["B29", "B14", "B1"]
#            , ["B29", "B12", "B1"]
#            , ["B29", "B13", "B1"]
#            , ["B29", "B11", "B1"]
#            , ["B29", "B18", "B1"]
#            , ["B29", "B28", "B26", "B1"]
#            , ["B29", "B27", "B26", "B1"]
#            , ["B29", "B20", "B19", "B1"]
#            , ["B29", "B25", "B1"]
#            , ["B29", "B10", "B8", "B1"]
#            , ["B29", "B24", "B23", "B1"]
#            , ["B29", "B22", "B21", "B1"]
#            , ["B29", "B6", "B1"]
#            , ["B29", "B4", "B2", "B1"]
#            , ["B29", "B3", "B1"]
#            , ["B29", "B7", "B5", "B1"]
#            , ["B29", "B9", "B1"]
#            ]


        runner.lineMap = \
            { "B29": 46
            , "B28": 47
            , "B27": 49
            , "B26": 52
            , "B25": 57
            , "B24": 59
            , "B23": 61
            , "B22": 63
            , "B21": 65
            , "B20": 67
            , "B19": 70
            , "B18": 79
            , "B17": 80
            , "B16": 81
            , "B15": 83
            , "B14": 86
            , "B13": 88
            , "B12": 96
            , "B11": 98
            , "B10": 100
            , "B9": 101
            , "B8": 103
            , "B7": 105
            , "B6": 106
            , "B5": 108
            , "B4": 110
            , "B3": 111
            , "B2": 113
            , "B1": 116
            , "B0": 122
            }

        self.minInput = 1
        self.maxInput = 5 

    def individual(self):
        return tools.initRepeat(creator.Individual, lambda: random.randint(self.minInput, self.maxInput), 3)

    def population(self, n):
        return tools.initRepeat(list, self.toolbox.individual, n)

def main():
    workPath = '.'
    binaryName = 'tritype'
    coverageToolPath = '/Users/zmay/Projects/clang-dev/build/bin/llvm-cov'
    runner = Runner(workPath, binaryName, coverageToolPath)
    t = Tritype(runner)
    results = t.runAll()
    print "GA complete on all paths, running all inputs..."
    for result in results:
        runner.runInput(result)
    print "Generating coverage report..."
    runner.dumpCoverageReporting()
    print "Done."

if __name__ == "__main__":
    main()

