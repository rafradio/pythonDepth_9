import os
import csv, json

class ClassForPrint:
    
    def __init__(self):
        self.PATH_TO_FILE = os.path.join(os.getcwd(), 'DumpedFiles', 'data.csv')
        self.PATH_TO_JSON = os.path.join(os.getcwd(), 'DumpedFiles', 'data.json')

    def dumpToCsv(self, func):
        
        def wrapNew(*args):
            print(func.__name__)
            # csv_data = func(*args)
            with open(self.PATH_TO_FILE, 'w', newline='', encoding='utf-8') as f_write:
                writer = csv.writer(f_write, dialect='excel', quotechar='"', quoting=csv.QUOTE_ALL)
                writer.writerows(func(*args))
            # return csv_data
            
        return wrapNew
    
    def dumpToJSON(self, func):
        def wrapNew():
            with open(self.PATH_TO_JSON, 'w', encoding='utf-8') as f:
                print(json.dumps(func(), indent=4, ensure_ascii=False), file=f)
            return
        
        return wrapNew