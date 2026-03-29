h=float(input("Enter your height="))
w=float(input("Enter your weight="))
bmi=w/(h/100)**2
print("BMI equals",bmi)

if bmi<=18.4:
    print("You are under weight")
elif bmi<=24.9:
    print("Your are healthy")
elif bmi<=29.9:
    print("You are over weight")
elif bmi <=34.9:
    print("Your are severely over weight")
elif bmi <=39.9:
    print("Your are obese")
else :
    print("You are severely obese")