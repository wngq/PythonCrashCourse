prompt = "\nTell me a topping you want:"
prompt += "\nEnter 'quit' to end the program."

while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print("We will add " + topping.title() + ".")
