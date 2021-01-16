from leap_year import leap_year

def days_in_a_month(year, month):
    if month < 1 or month > 12:
        return 'Invalid month'
    else:
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
        if leap_year(year):
            month_days[1] = 29
        return month_days[month - 1]


year = int(input('Enter a year: '))
month = int(input('Enter a month: '))
days = days_in_a_month(year, month)                 
print(days)