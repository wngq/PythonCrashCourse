sandwich_orders = ['tuna', 'green pepper', 'pastrami', 'beef', 'garlic', 'pastrami', 'pork', 'pastrami']
finished_sandwiches = []
# print(sandwich_orders)
print("I'm sorry, we're all out of pastrami today.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made your " + sandwich + " sandwich.")
    finished_sandwiches.append(sandwich)

print(finished_sandwiches)
