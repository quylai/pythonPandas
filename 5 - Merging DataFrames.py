#---------------------------------------------------------------------------------------
import pandas as pd

df1 = pd.read_csv(r"C:\Users\condr\Documents\pythonPandas\LOTR.csv")
df1

df2 = pd.read_csv(r"C:\Users\condr\Documents\pythonPandas\LOTR 2.csv")
df2


# merging df1 with df2; by default, method .merge see the first 2 rows has the same value on both dataframe for FellowshipID and FirstName; so it merge those 2 rows with the added cols "Skills" and "Age"
df1.merge(df2)


# explicit version of
# df1.merge(df2)
df1.merge(df2, how = "inner", on = ["FellowshipID", "FirstName"])


# merge everything from both df1 and df2; when no value available,
# "NaN" script would be in its place
df1.merge(df2, how = "outer")


# merging such that: everthing from df1 and those from df2 that are matched
# with df1
df1.merge(df2, how = "left")


# merging such that: everthing from df2 and those from df1 that are matched
# with df2
df1.merge(df2, how = "right")


# displaying all row of df2 for each row of df1
# very odd merging oO
df1.merge(df2, how = "cross")


# joining everything from df1 and df2, by criteria "FellowshipID";
# df1 is denoted by "_Left" and df2 is denoted by "_Right"
df1.join(df2, on = "FellowshipID", how = "outer", lsuffix = "_Left", rsuffix = "_Right")


"""
like code:
df1.join(df2, on = "FellowshipID", how = "outer", lsuffix = "_Left", rsuffix = "_Right")
.
which is joining everything from df1 and df2, by criteria "FellowshipID";
df1 is denoted by "_Left" and df2 is denoted by "_Right"
but the display of the table is much cleaner
"""
df4 = df1.set_index("FellowshipID").join(df2.set_index("FellowshipID"), lsuffix = "_Left", rsuffix = "_Right", how = "outer")
df4


# outer joining of df1 & df2, by axis 1
# recall: axis 0 refers to integer_inddex column
#         axis 1 refers to all the column names
pd.concat([df1,df2], join = 'outer', axis = 1)


















