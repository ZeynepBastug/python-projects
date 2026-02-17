
with open("weather-data.csv") as csvfile:
    data= csvfile.readlines()
print(data)


import csv


with open("weather-data.csv") as csvfile:
    data = csv.reader(csvfile)
    temperature = []
    for row in data:
        if row[1] != "Temp":
            temperature.append(int(row[1]))

print(temperature)