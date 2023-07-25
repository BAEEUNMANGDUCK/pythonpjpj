# # import csv

# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if 'temp' in row:
# #             continue
# #         else:
# #             temperatures.append(int(row[1]))
# #     print(temperatures)


# import pandas as pd


# data = pd.read_csv('weather_data.csv')
# print(type(data))

# print(data)
# print(data['temp'])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data['temp'].to_list()
# print(temp_list)


# # avg_temp = sum(temp_list)/ len(temp_list)
# # print(avg_temp)

# print(data['temp'].mean())

# print(data['temp'].max())


# # Get Data in Columns 
# cond1 = data.day == 'Monday'
# monday_row = data.loc[cond1,:]
# print(monday_row)
# monday_temp = int(monday_row.temp)
# monday_temp_to_fahrenheit = (monday_temp * 1.8) + 32 
# print(monday_temp_to_fahrenheit)


# # Get row getting highest temperature

# cond2 = data.temp == data.temp.max()

# highest_temp = data.loc[cond2,:]
# print(highest_temp)

# # Create a dataFrmae from scratch 


# data_dict = {
#     "students": [
#         "Amy", "James", "Angela"
#     ],
#     "scores": [76, 56, 65]
# }

# data = pd.DataFrame(data_dict)

# data.to_csv("new_data.csv")


import pandas as pd


squirrel_data = pd.read_csv('squirrel.csv')

cond1 = squirrel_data['Primary Fur Color'] == 'Gray'
cond2 = squirrel_data['Primary Fur Color'] == 'Cinnamon'
cond3 = squirrel_data['Primary Fur Color'] == 'Black'

gray = len(squirrel_data[cond1])
cinnamon = len(squirrel_data[cond2])
black = len(squirrel_data[cond3])

squirrel_count = pd.DataFrame(
    {
        'Fur color':['grey', 'red', 'black'],
        'Count':[gray,cinnamon, black]
    }
)

squirrel_count.to_csv('squirrel_count.csv')

