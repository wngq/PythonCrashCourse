import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'sitka_weather_2014.csv'

# 从文件中获取最高气温
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, "Missing Data....")
        else:
            # print(current_date)
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
            # print(dates)
            # print(highs)
            # print(lows)

    # 根据数据绘制图形
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # 设置图形格式
    plt.title("Daily high and low temperature - 2014\nStika", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()  # 绘制斜的日期标签
    plt.ylabel('Temperature(F)', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()
