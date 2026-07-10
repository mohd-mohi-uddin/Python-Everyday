from pathlib import Path
import pandas as pd

DATA_PATH = Path(__file__).parent

# # with open(DATA_PATH /"weather_data.csv") as data:
# #     data_list = data.readlines()
# #     print(data_list)


data = pd.read_csv(DATA_PATH /"weather_data.csv")
# print(data["temp"].to_list())
print(data[data.temp == data.temp.max()])