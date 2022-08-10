ht=float(input("What is your height (in inches)?"))
wt=float(input("What is your weight (in lbs)?"))
bmi = 703 * wt / ht ** 2
print("Your BMI is: ", bmi)
if bmi < 16:
    print("Very Severly Underweight.")
elif bmi >= 16 and bmi < 17:
    print("Severely underweight.")
elif bmi >=17 and bmi <18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi < 25:
    print("Normal (healthy weight)")
elif bmi >= 25 and bmi < 30:
    print("Overweight.")
elif bmi >= 30 and bmi < 35:
    print("Obese Class I (moderately obese)")
elif bmi >= 35 and bmi < 40:
    print("Obese Class II (Severely Obese)")
elif bmi >= 40 and bmi < 45:
    print("Obese Class III (Very Severely Obese)")
elif bmi >= 45 and bmi < 50:
    print("Obese Class IV (Mobidly Obese)")
elif bmi >= 50 and bmi < 60:
    print("Obese Class V (Super Obese)")
elif bmi >= 60:
    print("Obese Class VI (Hyper Obese)")