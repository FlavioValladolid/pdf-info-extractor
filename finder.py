
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
                print(ext.pdfReader_(root+'\\'+name_))
                df = df.append(pd.DataFrame([ext.pdfReader_(root+'\\'+name_)]))

# df.columns = list(items_dictionary.keys())
df.to_csv('file_name1.csv')