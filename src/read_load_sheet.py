import pandas as pd

class ReadLoadSheet():
    
    def __init__(self, load_sheet):
        self.load = load_sheet
        self.db_list = [] # lists of DBs with their loads as dictionaries
        
        
    def read_loads(self):
        return self.load([0, 0])