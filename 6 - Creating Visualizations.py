import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\condr\Documents\pythonPandas\Ice Cream Ratings.csv")
df = df.set_index("Date")
df

df.plot(kind = "line", title = "Ice Cream Ratings", xlabel = "Daily Ratings", ylabel = "Scores")

df.plot(kind = "line", subplots = True)


df.plot(kind = "bar", stacked = True)

df["Flavor Rating"].plot(kind = "bar", stacked = True)

df.plot.barh(stacked = True)


df.plot.scatter(x = "Texture Rating", y = "Overall Rating")

df.plot.scatter(x = "Texture Rating", y = "Overall Rating", s = 500, c = "Yellow")


df.plot.hist(bins = 10)


df.boxplot()


df.plot.area(figsize = (10,5))


df.plot.pie(y = "Flavor Rating", figsize = (10,10))


# different style of graphs
print(plt.style.available)
plt.style.use("classic")