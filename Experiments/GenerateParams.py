
from os import walk
import os



save_as = "./src/run/fsp50.sh"
problemSize = 20
numberOfruns = 20
stdevs = [0.001, 0.002, 0.003]
elit = [0]
path =  "./Taillard_instances/"
resultsPath = "./Results/"
parameters_to_print = "X_PARAM=("

problemNames = {"20": ["tai20_5_0.fsp", "tai20_5_1.fsp", "tai20_5_2.fsp", "tai20_5_3.fsp", "tai20_5_4.fsp",
           "tai20_5_5.fsp", "tai20_5_6.fsp", "tai20_5_7.fsp", "tai20_5_8.fsp", "tai20_5_9.fsp",
           "tai20_10_0.fsp", "tai20_10_1.fsp", "tai20_10_2.fsp", "tai20_10_3.fsp", "tai20_10_4.fsp",
           "tai20_10_5.fsp", "tai20_10_6.fsp", "tai20_10_7.fsp", "tai20_10_8.fsp", "tai20_10_9.fsp",
           "tai20_20_0.fsp", "tai20_20_1.fsp", "tai20_20_2.fsp", "tai20_20_3.fsp", "tai20_20_4.fsp",
           "tai20_20_5.fsp", "tai20_20_6.fsp", "tai20_20_7.fsp", "tai20_20_8.fsp", "tai20_20_9.fsp"],
           "50": ["tai50_5_0.fsp", "tai50_5_1.fsp", "tai50_5_2.fsp", "tai50_5_3.fsp", "tai50_5_4.fsp",
           "tai50_5_5.fsp", "tai50_5_6.fsp", "tai50_5_7.fsp", "tai50_5_8.fsp", "tai50_5_9.fsp",
           "tai50_10_0.fsp", "tai50_10_1.fsp", "tai50_10_2.fsp", "tai50_10_3.fsp", "tai50_10_4.fsp",
           "tai50_10_5.fsp", "tai50_10_6.fsp", "tai50_10_7.fsp", "tai50_10_8.fsp", "tai50_10_9.fsp",
           "tai50_20_0.fsp", "tai50_20_1.fsp", "tai50_20_2.fsp", "tai50_20_3.fsp", "tai50_20_4.fsp",
           "tai50_20_5.fsp", "tai50_20_6.fsp", "tai50_20_7.fsp", "tai50_20_8.fsp", "tai50_20_9.fsp"],
           "100": ["tai100_5_0.fsp", "tai100_5_1.fsp", "tai100_5_2.fsp", "tai100_5_3.fsp", "tai100_5_4.fsp",
            "tai100_5_5.fsp", "tai100_5_6.fsp", "tai100_5_7.fsp", "tai100_5_8.fsp", "tai100_5_9.fsp",
            "tai100_10_0.fsp", "tai100_10_1.fsp", "tai100_10_2.fsp", "tai100_10_3.fsp", "tai100_10_4.fsp",
            "tai100_10_5.fsp", "tai100_10_6.fsp", "tai100_10_7.fsp", "tai100_10_8.fsp", "tai100_10_9.fsp",
            "tai100_20_0.fsp", "tai100_20_1.fsp", "tai100_20_2.fsp", "tai100_20_3.fsp", "tai100_20_4.fsp",
            "tai100_20_5.fsp", "tai100_20_6.fsp", "tai100_20_7.fsp", "tai100_20_8.fsp", "tai100_20_9.fsp"],
           "200":["tai200_10_0.fsp", "tai200_10_1.fsp", "tai200_10_2.fsp", "tai200_10_3.fsp", "tai200_10_4.fsp",
            "tai200_10_5.fsp", "tai200_10_6.fsp", "tai200_10_7.fsp", "tai200_10_8.fsp", "tai200_10_9.fsp",
            "tai200_20_0.fsp", "tai200_20_1.fsp", "tai200_20_2.fsp", "tai200_20_3.fsp", "tai200_20_4.fsp",
            "tai200_20_5.fsp", "tai200_20_6.fsp", "tai200_20_7.fsp", "tai200_20_8.fsp", "tai200_20_9.fsp"],
           "500":["tai500_20_0.fsp", "tai500_20_1.fsp", "tai500_20_2.fsp", "tai500_20_3.fsp", "tai500_20_4.fsp",
            "tai500_20_5.fsp", "tai500_20_6.fsp", "tai500_20_7.fsp", "tai500_20_8.fsp", "tai500_20_9.fsp"]
           
           } 
count = 0
for problemSize in problemNames.keys():
    for probName in problemNames[problemSize]:
        popSizes = [ int(problemSize) * 10, int(problemSize) * 30, int(problemSize) * 50]
        if ("tai20_5" in probName.replace("-", "_")):
            FEs = 182224100
        elif ("tai20_10" in  probName.replace("-", "_")):
            FEs = 224784800
        elif("tai20_20" in probName.replace("-", "_")):
            FEs = 256896400
        elif("tai50_5" in probName.replace("-", "_")):
            FEs = 220712150
        elif("tai50_10" in probName.replace("-", "_")):
            FEs = 256208100
        elif("tai50_20" in probName.replace("-", "_")):
            FEs = 275954150
        elif("tai100_5" in probName.replace("-", "_")):
            FEs = 235879800
        elif("tai100_10" in probName.replace("-", "_")):
            FEs = 266211000
        elif("tai100_20" in probName.replace("-", "_")):
            FEs = 283040000
        elif("tai200_10" in probName.replace("-", "_")):
            FEs = 272515500
        elif("tai200_20" in probName.replace("-", "_")):
            FEs = 287728850
        elif("tai500_20" in probName.replace("-", "_")):
            FEs = 260316750


        for populationSize in popSizes:
            tSizes = [(round(int(populationSize) * 0.10)),(round(int(populationSize) * 0.25))]
            for truncSize in tSizes:
                for variance in stdevs:
                    for elitism in elit:
                        for run in range(numberOfruns):
                            saveAs = probName.replace(".fsp", "").replace("-", "_") + "P" + str(populationSize) + "T" + str(truncSize) + "V" + str(variance) + "E" + str(elitism) + "run" + str(run) + ".xlsx"
                            count = count +1 
                            parameters_to_print += ("\"" + str(populationSize) + " " + path + " " + probName + " "
                                        + str(FEs) + " " + str(truncSize) + " " + str(elitism) + " " + str(variance) + " " + resultsPath
                                        + " " + saveAs + "\" " )

parameters_to_print+=')'

start_string = '''#!/bin/bash --login
#$ -cwd
#$ -t 1-'''
start_string+=str(count) + '\n'

start_string+= '''
# Load the version you require
module load apps/anaconda3/5.2.0'''

start_string+='\n\n'

parameters_to_print = start_string + parameters_to_print


parameters_to_print += ''' \n\n# Bash arrays use zero-based indexing but you CAN'T use -t 0-9 above (0 is an invalid task id)
INDEX=$((SGE_TASK_ID-1))

# Run the app with one of the parameters
python RunRKEDA.py ${X_PARAM[$INDEX]}'''

#print(parameters_to_print)

text_file = open("./fsp.txt", "w")
n = text_file.write(parameters_to_print)
text_file.close()


