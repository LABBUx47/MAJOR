# 1. BMI Calculator with Category Takes a user's height and weight, then calculates their Body
# Mass Index. Uses if/elif/else to classify the result as underweight, normal, overweight, or obese,
# printed with a formatted message.

print("========== BMI CALCULATOR ==========")
print()

weight_kg = int(input("what is your weight (kg):"))
height_cm = float(input("enter your height in (cm):"))
height_m = height_cm / 100

bmi = round(weight_kg / (height_m * height_m), 2)  # bmi calculation (round will answer to 2 decimal)

print(f"Weight : {weight_kg} kg")
print(f"Height : {height_cm} cm")
print(f"BMI    : {bmi} kg/m²")

if bmi < 18.5:
    print("***Underweight***")

elif 18.5 <= bmi < 25:
    print("***Normal***")

elif 25 <= bmi < 30:
    print("***Overweight***")













#1st: i ask only for the formula of bmi bcz i don't know that





#2st error(no need of ai bcz when i see error hten i realize the problum is bcz of data type)
#PS C:\Users\lover.DESKTOP-F7NQEQ7\OneDrive\Desktop\python_lab_ex\MAJOR> python -u "c:\Users\lover.DESKTOP-F7NQEQ7\OneDrive\Desktop\python_lab_ex\MAJOR\bmi_cal.py"
# what is your weight(kg):12
# enter your height in (m):1.72
# Traceback (most recent call last):
#   File "c:\Users\lover.DESKTOP-F7NQEQ7\OneDrive\Desktop\python_lab_ex\MAJOR\bmi_cal.py", line 5, in <module>
#     height =int(input(f"enter your height in (m):"))
#             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# ValueError: invalid literal for int() with base 10: '1.72'
# PS C:\Users\lover.DESKTOP-F7NQEQ7\OneDrive\Desktop\python_lab_ex\MAJOR> 


#3nd
# DESKTOP-F7NQEQ7\OneDrive\Desktop\python_lab_ex\MAJOR\bmi_cal.py"
# what is your weight(kg):70
# enter your height in (m):1.75
# your weight: 70 
# your height: 1.75 
# bmi22.857142857142858
# PS C:\Users\lover.DESKTOP-F7NQEQ7\OneDrive\Desktop\python_lab_ex\MAJOR> 



#4rd fixing with round of answer
# using round when defining the formula of bmi calculation




# print("========== BMI CALCULATOR ==========")
# print()

# weight_kg = int(input("What is your weight (kg): "))
# height_cm = float(input("Enter your height (cm): "))

# height_m = height_cm / 100
# bmi = round(weight_kg / (height_m * height_m), 2)

# if bmi < 18.5:
#     category = "Underweight"
# elif 18.5 <= bmi < 25:
#     category = "Normal"
# elif 25 <= bmi < 30:
#     category = "Overweight"
# else:
#     category = "Obese"

# print()
# print("Your details:")
# print(f"Weight : {weight_kg} kg")
# print(f"Height : {height_cm} cm")
# print(f"BMI    : {bmi:.2f}")
# print(f"Category: {category}")








