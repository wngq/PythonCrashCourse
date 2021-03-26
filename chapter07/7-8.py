sandwich_orders = ['tuna', 'green pepper', 'beef', 'garlic', 'pork']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made your " + sandwich + " sandwich.")
    finished_sandwiches.append(sandwich)

print(finished_sandwiches)
