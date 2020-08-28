
from RKEDA import *
import sys


populationSize = int(sys.argv[1]) 
path = sys.argv[2]
probName = sys.argv[3]
FEs = int(sys.argv[4])
truncSize = int(sys.argv[5])
elitism = (int(sys.argv[6]) != 0)


initialStdev = float(sys.argv[7])
resultsPath = sys.argv[8]
saveAs = sys.argv[9]


alg = RKEDA(populationSize, path, probName, FEs, truncSize, elitism, initialStdev, resultsPath, saveAs)
alg.runEDA()