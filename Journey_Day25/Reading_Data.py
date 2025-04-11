# with open("weather_data.csv") as names_file:
#     names=names_file.readlines()
#     print(names)
#
# import csv
# with open("weather_data.csv") as names_file:
#     data=csv.reader(names_file)
#     temperatures=[]
#     for row in data:
#         if row[1]!='temp':
#             print(row)
#             temperatures.append(int(row[1]))
# print(temperatures)

import pandas as pd
from numpy.ma.extras import average

data=pd.read_csv("weather_data.csv")
# print(data)
# print(data['temp'])

# data_to_Dict=data.to_dict()
# print(data_to_Dict)

# temp_list=data['temp'].to_list()
# print(average(temp_list))

# print(data['temp'].mean())

# print(data['temp'].max())

# print(data['condition'])
# print(data.condition)

print(data[data.day=="Monday"])

print(data[data['temp']==max(data['temp'])])

monday_row=data[data.day=="Monday"]
print(monday_row.condition)

print((monday_row.temp))

data_dict = {
    "students":["Amy","James","Angela"],
    "scores":[76,56,65]
}

dataset=pd.DataFrame(data_dict)
dataset.to_csv("dataset.csv")

