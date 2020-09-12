
from RKEDA import *



populationSize = 200
path = "./Taillard_instances/"
probName = "tai20_5_0.fsp"
FEs = 182224100
truncSize = 20
elitism = False
stdev = 0.387

resultsPath = "./Results/"
saveAs = "tai20_5_0P200T20V0.387E0run0.xlsx"



alg = RKEDA(populationSize, path, probName, FEs, truncSize, elitism, stdev, resultsPath, saveAs)
alg.runEDA()