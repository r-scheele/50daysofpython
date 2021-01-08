print('Welcome to python pizza deliveries')

small_pizza = 15
medium_pizza = 20
large_pizza = 25
bill = 0

pizza_size = input("What size of pizza do you want? \nEnter  S for small size, M for medium and L for large ").upper()

if 'S' in pizza_size:
    bill += small_pizza
    print(f"Your current bill is ${bill}")
elif 'M' in pizza_size:
    bill += medium_pizza
    print(f"Your current bill is ${bill}")
elif 'L' in pizza_size:
    bill += large_pizza
    print(f"Your current bill is ${bill}")
else:
    print('Please enter current size format')

add_pepperoni = input('Do you want pepperoni? Y or N ').upper()
yes = 'Y' in add_pepperoni
if yes:
    if 'S' in pizza_size:
        bill += 2
        print(f"Your current bill is ${bill}")
    elif 'M' in pizza_size or 'L' in pizza_size:
        bill += 3
        print(f"Your current bill is ${bill}")

extra_cheese = input('Do you want extra cheese? Y or N ').upper()
if 'Y' in extra_cheese:
    bill += 1
print(f"Your final bill is ${bill}")
