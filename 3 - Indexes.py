#---------------------------------------------------------------------------------------
import pandas as pd

df = pd.read_csv(r"C:\Users\condr\Documents\pythonPandas\world_population.csv")
df


# index df by "Country" while assigning to df variable
df = pd.read_csv(r"C:\Users\condr\Documents\pythonPandas\world_population.csv", index_col = "Country")
df


# reset df back to default indices
df.reset_index(inplace=True)
df


# set df to index by "Country"
df.set_index("Country", inplace=True)
df


# display entry (row) "Albania"
df.loc["Albania"]


# displaying same as above, by accessing its default index
df.iloc[1]


df.reset_index(inplace=True)  # reset df to default index
# set df to indexing by "Continent" and "Country"
df.set_index(["Continent", "Country"], inplace=True)
# sorting alphabetically, by "Continent", then by "Country"
df.sort_index()

# setting change to display max 235 rows
pd.set_option('display.max.rows', 235)


# display index ["Africa", "Angola"]
df.loc["Africa", "Angola"]


# notice that it displayed Country Albania, that's because
# keyword "iloc" strictly accessing default original integer indices
df.iloc[1]
















