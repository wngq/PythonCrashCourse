import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [x ** 3 for x in x_values]

plt.scatter(x_values, y_values, edgecolors='none', s=30)

plt.title("Cube Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
