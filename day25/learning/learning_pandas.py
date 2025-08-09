
import pandas as pd

data = pd.read_csv("weather_data.csv")

print(f"\nType of data: {type(data)}\n")

print("Printing the Dataframe:\n")
print(data)


print("\nChecking out a Series:\n")
print(f"\nType of data['temp']: {type(data['temp'])}")
print(data["temp"])


print("\nTO_DICT-----------------------------#")
data_dict = data.to_dict()
print(data_dict)

print("\nTO_LIST-----------------------------#")
temp_list = data["temp"].to_list()
print(temp_list)


# calculating the average temp

avg_temp = sum(temp_list) / len(temp_list)
print(round(avg_temp, 2))

# OR

avg_temp_pandas = data["temp"].mean()
print(round(avg_temp_pandas, 2))

# getting max value

max_temp = data["temp"].max()
print(max_temp)

# get data in Columns
# both below are ok
print(data["condition"])
print(data.condition)

# get data from Rows
print("\nROWS--------------------------------#")
print(data[data.day == "Monday"])

# small challenge / getting data in a row where the temperature is highest
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)

# get monday temp convert them to fahrenheit
print(monday.temp)
print((monday.temp * (9 / 5) + 32))


# Create a dataframe from scratch

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

new_data = pd.DataFrame(data_dict)
print(new_data)

new_data.to_csv("new_data.csv")