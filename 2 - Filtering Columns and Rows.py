#---------------------------------------------------------------------------------------
import pandas as pd

df = pd.read_csv(r"C:\Users\condr\Documents\pythonPandas\world_population.csv")

# of df, display only entries with Rank <= 10
df[df['Rank'] <= 10]


# of df, display entries in which col "Country" has values of variable
# specific_countries ("Bangladesh" and "Brazil")
specific_countries = ["Bangladesh","Brazil"]
df[df["Country"].isin(specific_countries)]


# of df, display entries in which col "Country" has str value of "United"
df[df["Country"].str.contains("United")]


# of df, make col "Country" as indices of rows and assign it to df2
df2 = df.set_index("Country")


# of df2, display only index (currently set as "Country"), "Continent" and "CCA#"
# axis = 1 (default if not written) means items search is of column headers
# axis = 0 means items search is of rows header (that is the row indices)
df2.filter(items = ["Continent", "CCA3"], axis = 1)


# of df2, search in axis = 0 (that is in rows indices), for items "Zimbabwe"
df2.filter(items = ["Zimbabwe"], axis = 0)


# of df2, search in axis = 0 (that is in rows indices), for items "United"
df2.filter(like = "United", axis = 0)


# of df2, in rows indices, locate a row in which its masked index
# contained value "United States"
df2.loc["United States"]


# of df2, locate the row with index of 3;
# even though row indices is masked, its numerical indices is still there
df2.iloc[3]


# of df, display countries with rank > 10; sorted as followed:
# "Continent" ascending True, then,
# "Country" ascending True
df[df["Rank"] < 10].sort_values(by=["Continent","Country"],ascending=[True,True])
















