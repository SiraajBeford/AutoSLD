# import libraries
import pandas as pd
import os

# Import written packages
from src.read_load_sheet import ReadLoadSheet

# Read in load sheet
os.chdir('data')
load_sheet = pd.read_excel('lighting.xlsx')
print(load_sheet)

# TODO single line diagrams for one lighting circuit from load sheet
load_sheet = ReadLoadSheet(load_sheet)
load_sheet.read_loads()


# get criteria for single line diagrams
# process lighting requirement to nearest breaker (upward)
# TODO: Example criteria include alumnium cables or copper cables, types of circuit breakers, fault ratings, % voltage drop


# process criteria to single line diagrams
# Convert to tree table



# write to single line diagram on a pdf
# TODO write to a pdf