import pandas as pd
weather = pd.read_csv("D:\Python\day 25\weather_data.csv")
temp = weather["temp"].to_list()
# old avg method
# avg_temp = 0
# for each in temp:
#     avg_temp += each
# avg_temp = round(avg_temp/len(temp), 2)
# print(avg_temp)

# # new avg method
# print(weather["temp"].mean())
# # pandas max in series
# print(weather["temp"].max())
print(weather[weather.day == "Monday"])
