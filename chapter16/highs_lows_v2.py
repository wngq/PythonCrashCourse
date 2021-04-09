import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'sitka_weather_07-2014.csv'

# 从文件中获取最高气温
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        # print(current_date)
        dates.append(current_date)
        highs.append(int(row[1]))
    # print(dates)
    # print(highs)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')

# 设置图形格式
plt.title("Daily high temperature, July 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()  # 绘制斜的日期标签
plt.ylabel('Temperature(F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
