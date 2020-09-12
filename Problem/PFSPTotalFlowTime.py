import copy

import numpy as np
from numba import njit

class PFSPTotalFlowTime:

    # def __init__(self, path):
    #     #self.processingTimes = None
    #     self.path = path
    #     f = open(path, "r")

    #     doc = f.read()
    #     print(f.read())

    #     lines = doc.split("\n")
    #     processingTimes = []


    #     for i in range(len(lines)):
    #         values  = lines[i].split()
    #         if i == 1:
    #             jobs = int(values[0])
    #             machines = int(values[1])
    #             self.optimum = int(values[3])
    #             #print("jobs " , jobs, ", machines ", machines, "optimum ", self.optimum)
    #         elif((i > 2) and (i <= (machines + 2))):
    #             arr = []
    #             for j in range(jobs):
    #                 val = int(values[j])
    #                 arr.append(val)
    #             processingTimes.append(arr)

    #     self.processingTimes = copy.deepcopy(processingTimes)
    #     self.probSize = jobs

    
    def __init__(self, path):
        #self.processingTimes = None
        self.path = path
        f = open(path, "r")

        doc = f.read()
        print(f.read())

        lines = np.array(doc.split("\n"))
        

        values  = lines[1].split()
        jobs = int(values[0])
        machines = int(values[1])
        self.optimum = int(values[3])

        processingTimes = []

        for i in range(len(lines)):
            values  = lines[i].split()
            if((i > 2) and (i <= (machines + 2))):
                arr = []
                for j in range(jobs):
                    val = int(values[j])
                    arr.append(val)
                processingTimes.append(arr)
        self.processingTimes = np.array(copy.deepcopy(processingTimes))
        self.probSize = jobs

    
    def evaluate(self, genes):
        processingTimes = copy.deepcopy(self.processingTimes)
        n_machines = len(processingTimes)
        n_jobs = len(processingTimes[0])
        m_timeTable = np.array([0]*n_machines)
        solution = np.array(copy.deepcopy(genes))
        fitness = PFSPTotalFlowTime.computeFitness(processingTimes, n_machines, n_jobs, m_timeTable, solution)
        return fitness

        
    @njit
    def computeFitness(processingTimes, n_machines, n_jobs, m_timeTable, genes):
        for i in range(n_machines):
            first_gene=genes[0]
            m_timeTable[0]=processingTimes[0][first_gene]
            for k in range(n_machines-1):
                j = k+1
                m_timeTable[j]=m_timeTable[j-1]+processingTimes[j][first_gene]

        fitness=m_timeTable[n_machines-1]
        for y in range(n_jobs-1):
            job=genes[y + 1]
            m_timeTable[0]+=processingTimes[0][job]
            prev_machine=m_timeTable[0]

            for m in range(n_machines-1):
                machine = m+ 1
                m_timeTable[machine]= max(prev_machine,m_timeTable[machine])+ processingTimes[machine][job]
                prev_machine=m_timeTable[machine]
            
            fitness+=m_timeTable[n_machines-1]

        return fitness


    def getProblemSize(self):
        return self.probSize

            
    def getOptimalFitness(self):
        return self.optimum