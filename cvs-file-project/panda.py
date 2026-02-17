import pandas as panda

print(panda.__version__)

data = panda.read_csv("weather-data.csv")

print(data)

print(data["Temp"])

data_dict = data.to_dict()
print(data_dict)

data_as_list = data["Temp"].to_list()
print(data_as_list)

print("---------------------------------")

sum = sum(data_as_list)
size = len(data_as_list)

average = round(sum / size)
print(average)
# mean() for average
print(data["Temp"].mean())

print(data["Temp"].max())
print(data["Temp"].min())


print(data["Temp"].max())

print("---------------------------------")
#Get Data in Row
print(data[data.Day == "Monday"])

print("---------------------------------")
print(data[data.Temp == data.Temp.max()])

print("---------------------------------")
monday = data[data.Day == "Monday"]
print(monday.Condition)

print("---------------------------------")
monday_temp = monday.Temp[0]
monday_temp_F = monday_temp * 9/5 +32
print(monday_temp_F)

print("---------------------------------")
data_dict2 = {
    "students" : ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = panda.DataFrame(data_dict2)
print(data)
data.to_csv("new_data.csv")