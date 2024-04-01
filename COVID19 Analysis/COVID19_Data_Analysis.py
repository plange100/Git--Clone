#COVID19 Data analysis

import pandas as pd
import numpy as npo
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("covid19.csv")

print(df.head(10))
print(df.info())
print(df.shape)

#Drop unwanted columns
#df.drop(["FIPS", "Admin2", "Lat", "Long_", "Last_Update", "Combined_Key"], axis=1, inplace=True)
# print(df.info())

#Aggregate by country/region using groupby and summing
#df_sum = df.groupby("Country_Region").sum()
#print(df_sum)
#print(df_sum.shape)

#create histogram between various countries
#df_sum.loc[0].plot()
