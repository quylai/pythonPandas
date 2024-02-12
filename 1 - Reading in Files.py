#---------------------------------------------------------------------------------------

import pandas as pd

# read in a .csv file 
df = pd.read_csv(r"C:\Users\condr\Documents\pythonPandas\countries of the world.csv")

# read in a .txt file
df = pd.read_table(r"C:\Users\condr\Documents\pythonPandas\countries of the world.txt")

# read in a .json file
df = pd.read_json(r"C:\Users\condr\Documents\pythonPandas\json_sample.json")

# read in a .xlsx file, 1st sheet
df = pd.read_excel(r"C:\Users\condr\Documents\pythonPandas\world_population_excel_workbook.xlsx")

# read in a .xlsx file with specified sheet name
df2 = pd.read_excel(r"C:\Users\condr\Documents\pythonPandas\world_population_excel_workbook.xlsx", sheet_name = "Sheet1")

# set specified max rows displayed
pd.set_option("display.max.rows", 235)

# set specified max cols displayed
pd.set_option("display.max.columns", 40)

# display information about dataframe df2
df2.info()

# display dimension of df2
df2.shape

# display first 10 row
df2.head(10)

# display last 10 row
df2.tail(10)

# display only col "Rank" of dataframe df2
# df2['Rank']
df2["Rank"]

# searching for string value "Uzbekistan" in df2
# df2.loc['Uzbekistan']  # erroring, why?
# df2.loc["Uzbekistan"]  # erroring, why?

# searching df2 with row_index_224
df2.iloc[224]

