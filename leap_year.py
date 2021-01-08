# if the year is divisible by 4
# if the year is not divisible by 100 and also not divisible by 400
def leap_year(year):
    year = int(year)

    if(len(str(year)) != 4):
        return "Please enter correct year format"

    res = "This is leap year" if (year%4 == 0 and (year%100 != 0 and year%400 != 0)) else "This is not a leap year"
    return res

print(leap_year(2020))