#COVID19 Data analysis

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("csv/covid19.csv")
happy_df = pd.read_csv("csv/2019.csv")

# print(df.head(10))
# print(df.info())
# print(df.shape)

#Drop unwanted columns
df.drop(["Lat", "Long"], axis=1, inplace=True)
# print(df.info())

#Aggregate by country/region using groupby and summing
df_sum = df.groupby("Country/Region").sum()
# print(df_sum.head())
#print(df_sum.shape)

#create histogram between various countries
# df_sum.loc["China"].plot()
# df_sum.loc["Italy"].plot()
# plt.legend()

# df_sum.loc["China"][0:5].plot()
# df_sum.loc["Italy"][0:5].plot()
# plt.legend()

#calculate change in reate using derivative(diff())
# df_sum.loc["China"].diff().plot()
# df_sum.loc["Italy"].diff().plot()
# plt.legend()

# max infection rate per country
# ch = df_sum.loc["China"].diff().max()
# it = df_sum.loc["Italy"].diff().max()
# sp = df_sum.loc["Spain"].diff().max()
# print([ch, it, sp])

countries = list(df_sum.index)
max_infection_rate = []
for c in countries:
  max_infection_rate.append(df_sum.loc[c].diff().max())
df_sum["max_infection_rate"] = max_infection_rate
# df_sum.head(10)

max_rate = pd.DataFrame(df_sum["max_infection_rate"])
# max_rate.head()

#delete unwanted colums
# happy_df.head()
happy_df.drop(["Overall rank", "Score", "Generosity", "Perceptions of corruption"], axis=1, inplace=True)
# happy_df.head()
happy_df.set_index("Country or region", inplace=True)
# happy_df.head()

data = max_rate.join(happy_df, how="inner")
# data.head()
#.corr correlates all rows and columns
# data.corr()

x_gdp = data["GDP per capita"]
y_inf_rate = data["max_infection_rate"]

# sns.scatterplot(data=data,x=x_gdp,y=np.log(y_inf_rate))

#regression plot
sns.regplot(data=data,x=x_gdp,y=np.log(y_inf_rate))

