import copy
from Representation import Orderings as Od

class RK:

    def __init__(self, randomkeys):
        self.fitness = None
        self.permutation = []
        self.randomkeys =  randomkeys.copy()


    def getFitness(self):
        return self.fitness
  

    def setFitness(self, fitness):
        self.fitness = fitness


    def getPermutation(self):
        return (self.permutation.copy())


    def  setPermutation(self, permutation):
        self.permutation = permutation.copy()

    def copyGene(self):
        return (self.randomkeys.copy())

 
    def copyOf(self):
        rk = RK(self.randomkeys.copy())
        rk.fitness = self.fitness
        rk.setPermutation(self.permutation.copy())
        return rk


    def normalise(self):
        self.randomkeys = Od.Orderings.normaliseRanks(self.permutation.copy()).copy()
        
    
    def print(self):
        return ("RK: " , self.randomkeys, "\n Permutation: " , self.permutation , "\n Fitness: " + self.fitness)
    