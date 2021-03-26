def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_model = unprinted_designs.pop()
        print("Printing model: " + current_model)
        completed_models.append(current_model)
    return completed_models


def show_completed_models(completed_models):
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

show_completed_models(print_models(unprinted_designs[:], completed_models))  # [:]创建列表的副本

# 原列表还在
print("\noriginal unprinted designs: ")
print(unprinted_designs)
