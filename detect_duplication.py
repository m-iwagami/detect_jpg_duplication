from tkinter import Tk
from tkinter.filedialog import askdirectory
import os
import hashlib
import pandas as pd

class DetecDuplicate:
    def __init__(self):
        pass
        
    def select_file(self):
        Tk().withdraw()
        path = askdirectory(title="Select a folder")
        walker = os.walk(path)
        unique_file = {}
        duplicate_list = []
        hash_filename = []
        for folder, sub_folder, files in walker:
            for file in files:
                filepath = os.path.join(folder,file)
                filename = os.path.basename(filepath)
                filehash = hashlib.md5(open(filepath, "rb").read()).hexdigest()
                row_dict = {'FileName': filename, 'hashID': filehash}
                hash_filename.append(row_dict)     
                
                if filehash in unique_file:
                    dup_dict = {'Duplicate_hashID': filehash}
                    duplicate_list.append(dup_dict)

                else:
                    unique_file[filehash] = path

        return duplicate_list, hash_filename                
    
        
    def save_outcomme(self, df, file_name):
        df = pd.DataFrame(data = df)
        df.to_csv(file_name)

        
    def run_code(self, file_name):
        filehash, result = self.select_file()
        df = self.save_outcomme(filehash, result)
        df.to_csv(file_name)
    
detect_dup = DetecDuplicate()
dup, df = detect_dup.select_file()
detect_dup.save_outcomme(dup, "duplicated_file.csv")
detect_dup.save_outcomme(df, "hashid_file.csv")
        
                 
                