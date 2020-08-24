import copy
import random as r
import scipy.stats as ss

class Orderings:

    @staticmethod
    def generateRandomRK(n):
        return [r.random() for i in range(n)]

    @staticmethod
    def randomKeyToAL(priorities):
        temp = list(ss.rankdata(priorities))

        return [int(i -1) for i in temp]

    @staticmethod
    def normaliseRanks(ranks1):
        size = len(ranks1)
        ranks = copy.deepcopy(ranks1)
        AL = [0] * size
        for i in range(size):
            AL[ranks[i]] = (float)((i)/(size-1))
        
        return AL


       
