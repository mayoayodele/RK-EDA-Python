import os
import pandas as pd

path = './Results'


paths = os.listdir(path)

#print(paths)



config_list = list(set([params.split('run')[0] for params in paths] ))

config_file_name = {}

for config in config_list:
    file_names = [temp for temp in paths if config in temp]
    config_file_name[config] = file_names
    
    
for names in  config_file_name.keys():   
    number_of_runs = len(names)
    for file_name in config_file_name[names]:
        file_path = path + '/' + file_name
        df = pd.read_excel(file_path)
        print(file_path)
        print(df)


    



