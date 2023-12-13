weight = float(input('Enter weight in kilograms: '))
height = float(input('Enter height in meters: '))

bmi = weight / (height * height)

if bmi <= 18.4:
    print('Body Mass Index - BMI is', round(bmi, 2), '.You are underweight.')
elif bmi <= 24.9:
    print('Body Mass Index - BMI is', round(bmi, 2), '.You have normal weight.')
elif bmi <= 39.9:
    print('Body Mass Index - BMI is', round(bmi, 2), '.You are overweight.')
else:
    print('Body Mass Index - BMI is', round(bmi, 2), '.You are obese.')