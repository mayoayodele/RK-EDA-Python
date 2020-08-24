from Representation import RK as RK
import copy
import numpy as np
import random as r

class EDAUtils:

    @staticmethod
    def getBestSolutionMin(populationOfRK):
        best = populationOfRK[0].copyOf()
        for i in range(len(populationOfRK)):
            s = populationOfRK[i].copyOf()
            if(s.getFitness() < best.getFitness()):
                best = s.copyOf()

        return best

    @staticmethod
    def getPMTruncationSelection(currentPopulation1,truncSize):
        selectedGenome = []
        currentPopulation = [sol.copyOf() for sol in currentPopulation1]
        matrix = []

        currentPopulation.sort(key=lambda x: x.fitness, reverse=False)

        selectedGenome = [currentPopulation[i].copyOf() for i in range(truncSize)]
        numberOfActivities = len(currentPopulation[0].copyGene())

        for i in range(numberOfActivities):
            s = []
            for j in range(truncSize):
                s.append(selectedGenome[j].copyGene()[i])
            temp_mean = np.mean(s)
            matrix.append(temp_mean)
        return matrix

    @staticmethod
    def getChild(currentModel1, sigma):
        currentModel = currentModel1.copy()
        child = []
        for i in range(len(currentModel)):
            mean = currentModel[i]
            val = np.random.normal(mean,sigma)
            child.append(val)
        return child

