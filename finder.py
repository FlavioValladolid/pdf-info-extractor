
import os
import extractor as ext
import pandas as pd

path = r"C:\Users\flavi\Documents\Orders - Printing and Converting"


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


a = list(df[2]) + list(df[3]) + list(df[4]) + list(df[5])   
print(a)
"""
for row in range(len(df.index)):
    if row == 1 or row == 2:
        pass
    else:
        a += list(df[row])

print(a)

"""

# df.columns = list(items_dictionary.keys())

# df.to_csv('file_name1.csv')