w = input("enter your weight in pounds: ")
h = input("enter your height in inches: ")
bmi = (float(w)*703) / (float(h)*float(h))
print("your BMI is : ", f"{bmi:.1f}")
if bmi < 18.5:
    print("you are underweight")
elif bmi >= 18.5 and bmi < 25:
    print("you are normal weight")
elif bmi >= 25 and bmi < 30:
    print("you are overweight")
elif bmi >= 30:
    print("you are obese")
else:
    print("error occured.")