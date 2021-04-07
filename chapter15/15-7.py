from die import Die
import pygal

die_1 = Die(8)
die_2 = Die(8)

results = []

for roll_num in range(0, 1000000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# print(results)
frequencies = []

max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# print(frequencies)
# 对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling two D8 1000000 times"
hist.x_labels = [str(x) for x in range(2, max_result + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D8+D8', frequencies)
hist.render_to_file('15-7-dice_visual.svg')
