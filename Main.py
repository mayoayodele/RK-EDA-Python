
from RKEDA import *



populationSize = 100
path = "./Taillard_instances/"
probName = "tai50_20_9.fsp"
FEs = 50000
truncSize = 20
elitism = False
stdev = 0.3

resultsPath = "./Results/"
saveAs = "tai50_20_9P500T50V0.1874496528878277e0run0.xlsx"



alg = RKEDA(populationSize, path, probName, FEs, truncSize, elitism, stdev, resultsPath, saveAs)
alg.runEDA()