import csv
import pandas


#without pandas: 

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     next(data)

#     temperatures = []
#     for row in data:
#         temperatures.append(int(row[1]))

#     print(temperatures)


#with pandas:

# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# average_temp = (data["temp"].mean())
# max_temp = (data["temp"].max())

# # get data in columns:
# print(data["condition"])
# print(data.condition)

# # get data in rows:
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_fahrenheit = monday_temp * 9/5 + 32
# print(monday_temp_fahrenheit)

#create dataframe from scratch:
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")