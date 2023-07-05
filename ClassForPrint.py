import os
import csv

class ClassForPrint:
    
    def __init__(self):
        self.PATH_TO_FILE = os.path.join(os.getcwd(), 'DumpedFiles', 'data.csv')

    def dumpToCsv(self, func):
        
        def wrapNew(*args):
            print(func.__name__)
            # csv_data = func(*args)
            with open(self.PATH_TO_FILE, 'w', newline='', encoding='utf-8') as f_write:
                writer = csv.writer(f_write, dialect='excel', quotechar='"', quoting=csv.QUOTE_ALL)
                writer.writerows(func(*args))
            # return csv_data
            
        return wrapNew