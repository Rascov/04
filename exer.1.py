weight = input(50)
height = input(165)

height = height / 100

bmi = weight / (height ** 2)
print(bmi)

if bmi < 18.5:
    print(f"Your BMI is {bmi:.2f} and you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi:.2f} and you are normal.")
elif bmi < 30:
    print(f"Your BMI is {bmi:.2f} and you are overweight.")
else:
    print(f'Your BMI is {bmi:.2f} and you are obese.')