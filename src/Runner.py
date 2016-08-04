import os
import re
import subprocess

class Runner:
    def __init__(self, workPath, binaryName, coverageToolPath, paths=None, lineMap=None):
        # This regex matches lines in the coverage reporting that indicate a basic
        # block was not covered.
        self.uncoveredMatcher = re.compile(' *\$\$\$\$\$:')
        self.paths = paths
        self.lineMap = lineMap

        self.workPath = workPath
        self.binaryName = binaryName
        self.coverageToolPath = coverageToolPath

        self.executablePath = os.path.join('.', self.workPath, self.binaryName + '-instr')
        self.coverageDataFilePath = self.binaryName + '.gcda'
        self.coverageReportingFilePath = os.path.join(workPath, self.binaryName + '.c.gcov')

        print "Executable path:", self.executablePath
        print "Coverage data path:", self.coverageDataFilePath
        print "Coverage reporting path:", self.coverageReportingFilePath

    # Run the instrumented binary, process the coverage data into a useful format
    # and load the result so it can be queried for block coverage.
    def run(self, *inputs):
        self.cleanup()
        self.runInput(inputs)
        self.fileContents = self.dumpCoverageReporting()

    def runInput(self, *inputs):
        process = subprocess.Popen([self.executablePath], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        inputString = "\n".join(map(str, inputs))
        process.communicate(inputString)

    def dumpCoverageReporting(self):
        subprocess.call([self.coverageToolPath, 'gcov', '-a', self.binaryName], stdout=subprocess.PIPE)
        return list(open(self.coverageReportingFilePath))


    # Reset the class for a subsequent run of the instrumented binary.
    def cleanup(self):
        if os.path.isfile(self.coverageDataFilePath):
            os.remove(self.coverageDataFilePath)
        if os.path.isfile(self.coverageReportingFilePath):
            os.remove(self.coverageReportingFilePath)
        self.fileContents = []

    # Returns true if the given basic block was covered in the last run of the
    # instrumented binary.
    def covered(self, bb):
        return self.uncoveredMatcher.match(self.fileContents[self.lineMap[bb]]) == None

    # Return a list of booleans, corresponding to the coverage status of a
    # list of basic blocks, identified by their basic block numbers as defined
    # by the keys of the coverage map.
    def pathCoverage(self, path):
        return map(self.covered, path)

    # Return a list of booleans, corresponding to the coverage status of the 
    # basic blocks defined as the keys in the coverageMap dictionary.
    def coverage(self):
        return self.pathCoverage(self.lineMap.keys())

    # Return the coverage fitness of a path coverage vector; i.e., how deep
    # in the coverage path we get before we find an uncovered block.
    # This is just the number of True values the coverage vector starts with.
    def pathCoverageFitness(self, path):
        pathCoverage = self.pathCoverage(path)
        value = 0
        for i in xrange(len(pathCoverage)):
            if pathCoverage[i]:
                value += 1
            else:
                return value
        return value

    
