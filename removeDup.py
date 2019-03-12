import pandas as pd
import numpy

df = pd.read_csv('flight.csv')
print df.shape
df.drop_duplicates(subset = [df.columns[0],df.columns[1],df.columns[3],df.columns[4],df.columns[6],df.columns[7],df.columns[8],df.columns[9]], inplace = True) 
print df.shape
pd.DataFrame(df).to_csv("updatedFlight.csv", header = None, index = None)





