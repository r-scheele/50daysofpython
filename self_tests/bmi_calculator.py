height = float(input('Enter your heigth in meters: '))
weight = float(input('Enter your weigth in kg: '))

bmi = round(weight / height ** 2)

result = ''
bmiStr = str(bmi)
if bmi <= 18.5:
    result += f'Your bmi is '+ bmiStr + ', Your slightly under weight'
    print(result)
elif 18 < bmi <= 25:
    result += 'Your bmi is '+ bmiStr + ', You have a normal weight'
    print(result)
elif 25 < bmi <= 30:
    result += 'Your bmi is '+ bmiStr + ', Your slightly over weight' 
    print(result)
elif 30 < bmi <= 35:
    result += 'Your bmi is '+ bmiStr + ", You're obese"
    print(result)
else:
    result += 'Your bmi is '+ bmiStr + ", You're clinically obese LOL..."
    print(result)

#under 18 -- under weigth
#over 18 but below 25 --- normal weight
#over 25 but below 30 ---- over weight
#over 30 but below 35 --- obese
#over 35  ---- clinically obese