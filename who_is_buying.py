import random

seed_number = int(input("Enter seed number: "))
random.seed(seed_number)

name_as_csv = input("Give me evrybody's name, seperated with a comma: ")
names = name_as_csv.split(', ')

who_is_buying = names[random.randint(0, len(names) - 1)]
print(f'{who_is_buying} is going to pay the bills today')