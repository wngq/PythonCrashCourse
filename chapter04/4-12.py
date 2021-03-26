my_foods = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
friend_foods = my_foods[:]  # 不能用friend_foods=my_foods, 这只是让两个变量指向同一个列表

friend_foods.append('111')

for my_food in my_foods:
    print(my_food)
print("-----------")
for friend_food in friend_foods:
    print(friend_food)