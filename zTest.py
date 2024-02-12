import pandas as pd


data = [[50, True], [40, False], [30, False]]
label_rows = ["Sally", "Mary", "John"]
label_cols = ["age", "qualified"]

df = pd.DataFrame(data, label_rows, label_cols)
df

# print(df.loc["Mary", "age"])

df.loc["30"]










