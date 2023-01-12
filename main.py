#Cleaninig the data 
# Importing libraries

import pandas as pd 
import numpy as np

# Read data in pandas data frame 
data = pd.read_csv("austin_weather.csv")
 # drop some unnecessary coloumn 

data = data.drop(['Events','Date','SeaLevelPressureHighInches','SeaLevelPressureLowInches'] , axis =1 )
data = data.replace('T',0.0)
data = data.replace('-',0.0)

# Saving Final Dataset
data.to_csv('Austin_final.csv')