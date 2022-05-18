from utils.contrast import CarContrast
import pandas as pd

tool = CarContrast()

data = pd.read_csv('/var/www/FlaskApp/FlaskApp/assets/car_new.csv')

all_data = dict()

for i in range(200):
    info = dict(data.iloc[i])
    for j in info.keys():
        info[j] = str(info[j])
    all_data[info['car_ID']] = info

all_addresses = dict()
for id in all_data.keys():
    address = tool.new(all_data[id])
    all_addresses[id] = [address]

tool.addresses = all_addresses
tool.df = data