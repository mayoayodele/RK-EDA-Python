import os
import pandas as pd
import numpy as np

path = './Results'


paths = os.listdir(path)

#print(paths)



config_list = list(set([params.split('run')[0] for params in paths] ))

config_file_name = {}

for config in config_list:
    file_names = [temp for temp in paths if config in temp]
    config_file_name[config] = file_names

#summary_results = pd.DataFrame(columns = ['Avg Execution Time', 'Avg Fitness', 'Fitness Evaluations', 'Permutation','problem Name'])
summary_results = []
for names in  config_file_name.keys():   
    number_of_runs = len(names)
    temp_results = pd.DataFrame(columns = ['Execution Time', 'Fitness', 'Fitness Evaluations', 'Permutation','problem Name', 'Config'])
    summary_results_dict = {}
    if('tai' in names):
        for file_name in config_file_name[names]:
            if('.xlsx' in file_name):
                file_path = path + '/' + file_name
                df = pd.read_excel(file_path)
                temp_results = pd.concat([temp_results,df.iloc[[-1]] ])
        best_fitness = float(np.min(temp_results[['Fitness']]))
        best_solution =  temp_results.loc[temp_results['Fitness'] == best_fitness]
        print(best_solution)
        index = int(best_solution.index[0])
 
        best_permutation = best_solution.at[index,'Permutation']
        problem_name = best_solution.at[index,'problem Name']
        number_of_runs = len(temp_results)
      
        summary_results_dict = {'Average Execution Time': float(np.mean(temp_results[['Execution Time']])),
                                'Average Fitness': float(np.mean(temp_results[['Fitness']])),
                                'Best Fitness': best_fitness,
                                'Average Fitness Evaluations': float(np.mean(temp_results[['Fitness Evaluations']])),
                                'Best Permutation': best_permutation,
                                'Problem Name': problem_name,
                                'Number of runs': number_of_runs,
                                'Config': names
                                }
      
        summary_results.append(summary_results_dict)
        print(summary_results)

df = pd.DataFrame.from_records(summary_results)

print(df)

df.to_excel('Summary.xlsx')



    



