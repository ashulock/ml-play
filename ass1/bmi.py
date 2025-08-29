weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))
bmi = weight / (height ** 2)

if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 24.9:
    category = "Normal weight"
elif 24.9 <= bmi < 29.9:
    category = "Overweight"
else:
    category = "Obese"

print(f"BMI: {bmi:.2f}, Category: {category}")