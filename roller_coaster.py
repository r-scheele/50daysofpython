height = int(input('Enter your height in cms: '))
bill = 0

if( height >= 120):
    age = int(input('Please enter your age: '))
    if age <= 12:
        bill += 5
        print(f"Childs tickets is ${bill}")
    elif age <= 18:
        bill += 7
        print(f"Youths tickets is ${bill}")
    else:
        bill += 12
        print(f"Adults tickets is ${bill}")

    wants_photo = input("Do you want a photo taken? Y or N ").upper()

    if('Y' in wants_photo):
        bill += 3
    else:
        bill

    print(f"Your final bill is {bill}")


else:
    print("Please come back when you grow taller")