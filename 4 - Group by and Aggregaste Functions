#---------------------------------------------------------------------------------------
import pandas as pd

df = pd.read_csv(r"C:\Users\condr\Documents\pythonPandas\Flavors.csv")
df


"""
group_by_frame = df.groupby("Base Flavor")
group_by_frame.mean()

above 2 codes line need to be written as:

group_by_frame = df.groupby("Base Flavor")
                  [["Flavor Rating", "Texture Rating", "Total Rating"]].mean()
                  
for some reason when using .mean() method, it needed to be specify with others
column that it's displaying with;
in this case "Flavor Rating", "Texture Rating", "Total Rating"
"""

# display grouping of "Base Flavor" (as index), and average of
# "Flavor Rating", "Texture Rating", "Total Rating"
group_by_frame = df.groupby("Base Flavor")[["Flavor Rating", "Texture Rating", "Total Rating"]].mean()
group_by_frame


# displaying the counts of rows for which it groupby "Base Flavor"
df.groupby("Base Flavor").count()


# displaying the sum-value of rows for which it groupby "Base Flavor"
df.groupby("Base Flavor").sum()


# displaying:
# groupby "Base Flavor", of it, 
#         there are "Flavor Rating" & "Texture Rating", of it
#             there are "mean", "max", "count", "sum"
df.groupby("Base Flavor").agg({"Flavor Rating": ["mean", "max", "count", "sum"],
                               "Texture Rating": ["mean", "max", "count", "sum"]
                               })


# displaying:
# groupby "Base Flavor" and "Liked", of it, 
#         there is "Flavor Rating", of it
#             there are "mean", "max", "count", "sum"
df.groupby(["Base Flavor","Liked"]).agg({"Flavor Rating": ["mean","max","count","sum"]})


# display general stats of "Base Flavor" groups
df.groupby("Base Flavor").describe()



