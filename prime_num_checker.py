
def prime_checker(number):
    number = int(number)
    for i in range(2, number - 1):
        if number % i == 0:
            return "It's not a prime number"
    return "It's a prime number"




n = int(input('Check this number: '))
print(prime_checker(number = n))