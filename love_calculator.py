name = input("What is your name? ")
crush_name = input("What is their name? ")
together = list(name.lower()) + list(crush_name.lower())
love = 0
true = 0
for i in 'true':
    love += together.count(i)
for i in 'love':
    true += together.count(i)

print(f"Your love life is {true}{love}% likely")
