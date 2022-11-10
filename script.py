import csv
import config
import os
import pandas as pd
df = pd.read_excel(config.summary_file)
df_list = df.values.tolist()
for i in df_list:
    profila_id=i[0]
    profila_saite=i[1]
    profila_vards=i[2]
    fails=i[3]
    if fails in os.listdir(config.csv_dir):
        df = pd.read_csv(config.csv_dir+fails, sep=';')
        df = df[['name','link']]
        df_list = df.values.tolist()
        for i in df_list:
            print(profila_id,"|",profila_saite, "|",profila_vards,"|",i[0],"|",i[1])
