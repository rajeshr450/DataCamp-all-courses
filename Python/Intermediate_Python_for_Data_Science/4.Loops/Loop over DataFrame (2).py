'''
The row data that's generated by iterrows() on every run is a Pandas Series. This format is not very convenient to print out. Luckily, you can easily select variables from the Pandas Series using square brackets:

for lab, row in brics.iterrows() :
    print(row['country'])

'''


# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Adapt for loop
for lab, row in cars.iterrows():
    print(str(lab) + ':', row["cars_per_cap"])
