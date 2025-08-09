import pandas as pd

SQUIRREL_DATA = "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"

squirrel_data = pd.read_csv(SQUIRREL_DATA)
squirrel_coats = squirrel_data["Primary Fur Color"]
squirrel_color_count = squirrel_coats.value_counts()
# squirrel_color_count.to_csv("squirrel_coat_count.csv")


# Angela's solution

data = pd.read_csv(SQUIRREL_DATA)
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pd.DataFrame(data_dict)
df.to_csv("squirrel_coat_count_angela.csv")