import pandas as pd 
import numpy as np 

df = pd.read_csv("country_vaccination_stats.csv")

df_country = df.groupby("country")

for i in (df_country.groups.keys()):

    mindv = np.nanmin(df_country.get_group(i)["daily_vaccinations"])
    
    df[df["country"] == i] = df[df["country"] == i].fillna(mindv)

    if all(df_country.get_group(i)["daily_vaccinations"].isnull()):

        df[df["country"] == i] = df[df["country"] == i].fillna(0)


