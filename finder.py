
import os
import extractor as ext
import pandas as pd

path = r"C:\Users\Flavio\Documents\Orders - Printing and Converting-20210726T191931Z-001\Orders - Printing and Converting"


df = pd.DataFrame([])
name_ = ''
for root, dirs, files in os.walk(path):
    for name in files:
        if name.endswith((".pdf")):
            name_ = name
            if 'PO' in name_:
                # print(ext.pdfReader_(root+'\\'+name_))
                path_file = ext.pdfReader_(root+'\\'+name_) 
                if len(path_file) == 1 or len(path_file) == 0:
                    print(f"Incomplete info of file {name_}")
                else:
                    print(f"Info of file {name_} added")
                    df = df.append(pd.DataFrame([path_file]))


a = list(df[2]) + list(df[3]) + list(df[4]) + list(df[5]) + list(df[6]) + list(df[7]) + list(df[8]) + list(df[9]) + list(df[10]) + list(df[11]) + list(df[12]) + list(df[13])  
# print(a)
"""
for row in range(len(df.index)):
    if row == 1 or row == 2:
        pass
    else:
        a += list(df[row])

print(a)

"""

# df.columns = list(items_dictionary.keys())
df2 = pd.Series(data = a)
df2.to_csv('colors.csv', index=False)
df.to_csv('file_name1.csv', index=False)