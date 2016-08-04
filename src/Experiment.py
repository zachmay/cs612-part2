import re
import os
import subprocess
from deap import creator, base, tools, algorithms

class Experiment:
    def __init__(self, runner):
        self.runner = runner
        self.toolbox = base.Toolbox()

        creator.create("FitnessMax", base.Fitness, weights=(1.0,))
        creator.create("Individual", list, fitness=creator.FitnessMax)

        self.populationSize = 50
        self.numberGenerations = 100
        self.crossoverProb = 0.5
        self.mutateProb = 0.1

        self.mate = tools.cxTwoPoint
        self.mutate = lambda individual: tools.mutUniformInt(individual, low=self.minInput, up=self.maxInput, indpb=0.05)
        self.select = lambda population, selectCount: tools.selTournament(population, selectCount, tournsize=3)

        self.toolbox.register("individual", self.individual)
        self.toolbox.register("population", self.population)
        self.toolbox.register("evaluate", self.evaluate)
        self.toolbox.register("mate", self.mate)
        self.toolbox.register("mutate", self.mutate)
        self.toolbox.register("select", self.select)

    def individual(self):
        pass

    def population(self, n):
        pass

    def evaluate(self, individual):
        self.runner.run(*individual)
        return [self.runner.pathCoverageFitness(self.currentPath)]

    def run(self, path):
        self.currentPath = path
        population = self.toolbox.population(n=self.populationSize) 
        return algorithms.eaSimple(population, self.toolbox, cxpb=self.crossoverProb, mutpb=self.mutateProb, ngen=self.numberGenerations, verbose=False)

    def runAll(self):
        results = []
        for path in self.runner.paths:
            (pop, debug) = self.run(path)
            results.append(pop[0])
            print (path, pop[0], pop[0].fitness)
        self.runner.cleanup()
        return results

