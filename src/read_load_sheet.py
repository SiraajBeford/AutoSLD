import pandas as pd
import os, os.path

class ReadLoadSheet():
    
    def __init__(self, directory):
        self.directory = directory
        self.db_list = [] # lists of DBs with their loads as dictionaries
        
        
    def read_schedules(self):
        os.chdir(self.directory)
        
        schedules = os.listdir()
        
        for schedule in schedules:
            self.db_list.append(pd.read_excel(schedule))
            
            
            
    def clean(self):
        for db in self.db_list:
            db.dropna()