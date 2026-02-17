import csv

import pandas as panda

data = panda.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

#print(data["Primary Fur Color"])

colors = ["Gray", "Black", "Red"]

list = [
    ["color" , "count"]
]
for color in colors:
    squirrel = [color, len(data[data["Primary Fur Color"] == "Gray"])]
    list.append(squirrel)

print(list)
df = panda.DataFrame(list)
print(df)
df.to_csv("squirrel_count.csv")