import numpy as np
import pandas as pd

dict1 = {
    "name" : ['Aditya','Rohan','Skillf','Shubh'],
    "marks" : [78,56,22,11],
    "city" : ["Siliguri","Jalpaiguri","Malda","Kolkata"]
}

df = pd.DataFrame(dict1)
print(df)

df.to_csv('friends.csv')