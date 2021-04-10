import csv
import matplotlib.pyplot as plt
from datetime import datetime


def get_weather_data(filename, dates, highs, lows):
    with open(filename) as f:
        reader = csv.reader(f)
        head_row = next(reader)
        for row in reader:
            try:
                current_date = datetime.strptime(row[0], '%Y-%m-%d')
                high = int(row[1])
                low = int(row[3])
            except:
                print(current_date, filename + " ---Missing Date....in file: " + filename)
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)


dates_1, highs_1, lows_1 = [], [], []
filename_1 = 'sitka_weather_2014.csv'
get_weather_data(filename_1, dates_1, highs_1, lows_1)

# 根据数据绘制图像
fig = plt.figure(dpi=128, figsize=(15, 9))
plt.plot(dates_1, highs_1, c='red', alpha=0.5)
plt.plot(dates_1, lows_1, c='blue', alpha=0.5)
plt.fill_between(dates_1, highs_1, lows_1, facecolor='blue', alpha=0.1)

dates_2, highs_2, lows_2 = [], [], []
filename_2 = 'death_valley_2014.csv'
get_weather_data(filename_2, dates_2, highs_2, lows_2)
plt.plot(dates_2, highs_2, c='red', alpha=0.5)
plt.plot(dates_2, lows_2, c='green', alpha=0.5)
plt.fill_between(dates_2, highs_2, lows_2, facecolor='green', alpha=0.1)

# 设置图像格式
plt.title("Daily high and low temperature - 2014\nDeath Vally and Stika", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
