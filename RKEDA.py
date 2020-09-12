from Problem import PFSPTotalFlowTime as PFSP
from Representation import RK as rk
from Representation import Orderings as Od
from Utils import EDAUtils as Utils
import pandas as pd
import copy 
import time

class RKEDA:

    def __init__(self,populationSize, path, probName, FEs, truncSize, elitism, stdev, resultsPath, saveAs):
        self.populationSize = populationSize
        self.path = path
        self.probName = probName
        self.FEs = FEs
        self.truncSize = truncSize
        self.elitism = elitism
        self.stdev = stdev
        self.resultsPath = resultsPath
        self.saveAs = saveAs

    
    def runEDA(self):
        isfirst = True
        path = self.path + self.probName
        populationSize = self.populationSize
        FEs = self.FEs
        truncSize = self.truncSize
        elitism = self.elitism
        permProb = PFSP.PFSPTotalFlowTime(path)
        probSize = permProb.getProblemSize()
        #optimal = permProb.getOptimalFitness()

        population = []
        temp_population = []
        count = 0

        results = []
        
        start_time = time.time()
        for i in range(populationSize):
            perm = rk.RK(Od.Orderings.generateRandomRK(probSize))
            perm.setPermutation(Od.Orderings.randomKeyToAL(perm.copyGene()))
            perm.normalise()
            perm.setFitness(permProb.evaluate(perm.getPermutation()))
            count = count + 1
            population.append(perm.copyOf())

        matrix = []
        best = Utils.EDAUtils.getBestSolutionMin(population).copyOf()
        matrix = copy.deepcopy(Utils.EDAUtils.getPMTruncationSelection(population, truncSize) )
      
        end_time = time.time()
        res = {'problem Name': self.probName,
                'Permutation': best.permutation,
                'Fitness': best.getFitness(),
                'Fitness Evaluations': count,
                'Execution Time': end_time - start_time
                }
                
        results.append(copy.deepcopy(res))
       

        gens = float (FEs/populationSize)
        weight = 1
        stdev = self.stdev * weight

        j = 0

        for gen in range(int(gens)):
            isfirst = True
            for i in range(populationSize):
                child = None
                if(isfirst and elitism):
                    child = best.copyOf()
                    isfirst = False
                else:
                    randomkey = Utils.EDAUtils.getChild(matrix, stdev)
                    child = rk.RK(randomkey.copy())
                    child.setPermutation(Od.Orderings.randomKeyToAL(child.copyGene()))
                    child.normalise()
                    child.setFitness(permProb.evaluate(child.getPermutation()))
                    count = count + 1
                    if (count == FEs):
                        break

                temp_population.append(child.copyOf())

        
  

            #population = []
            population = [sol.copyOf() for sol in temp_population]
            temp_population = []

            weight = 1 - float (j/gens)
            stdev = self.stdev * weight
            j = j + 1

            if (len(population) == populationSize):
                matrix = copy.deepcopy(Utils.EDAUtils.getPMTruncationSelection(population, truncSize))
            bestTemp = Utils.EDAUtils.getBestSolutionMin(population)
            
            if (bestTemp.fitness < best.fitness):
                print(str(gen) + ", Fitness: " +  str(bestTemp.fitness)) 
                best = bestTemp.copyOf()
                end_time = time.time()
                res = {'problem Name': self.probName,
                        'Permutation': best.permutation,
                        'Fitness': best.getFitness(),
                        'Fitness Evaluations': count,
                        'Execution Time': end_time - start_time
                        }
                results.append(copy.deepcopy(res))
       
        df = pd.DataFrame.from_records(results)

        print(df)

        df.to_excel(self.resultsPath +  self.saveAs )





