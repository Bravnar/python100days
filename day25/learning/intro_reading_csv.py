
# CSV stands for comma separated values

print("\nBUILT-IN---------------------------------#")

# way to extract data from a file using readlines
with open("weather_data.csv", "r") as data_file:
    data = data_file.readlines()
    print(data)

print("\nCSV--------------------------------------#")

# way to extract data from a csv file using csv module
import csv
with open("weather_data.csv", "r") as data_file:
    data = csv.reader(data_file) # creates a reader object
    # temperatures = [int(x[1]) for x in data if x[1] != 'temp']
    temperatures = []
    for row in data:
        print(row)
        if (row[1] != "temp"):
            temperatures.append(int(row[1]))

    print(data)
    print(temperatures)


print("\nPANDAS-----------------------------------#")
# and now how to do it with pandas
import pandas as pd

df = pd.read_csv("weather_data.csv")
print(df["temp"])