
from RKEDA import *


populationSize = int(sys.argv[0]) 
path = sys.argv[1]
probName = sys.argv[2]
FEs = int(sys.argv[3])
truncSize = int(sys.argv[4])
elitism = (int(sys.argv[5]) != 0)


initialStdev = float(sys.argv[6])
resultsPath = sys.argv[7]
saveAs = sys.argv[8]


alg = RKEDA(populationSize, path, probName, FEs, truncSize, elitism, initialStdev, resultsPath, saveAs)
alg.runEDA()