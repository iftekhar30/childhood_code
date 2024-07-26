
weight = float(input("Weight: "))
starting_weight = weight
height = float(input("Height: "))
age = float(input("Age: "))
goal = float(input("Goal Weight: "))

bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)

bmi = round(weight/(height/100) ** 2, 2)

bmr = bmr *1.55

print("")

week = 0
while weight < 60:

    bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    bmr = round(bmr *1.55, 2)
    bmi = round(weight/(height/100) ** 2, 2)

    week += 1
    weight += 1

    print(f"Week: {week}")
    print(f"Calorie Consumed = {bmr+1000} (maintenance : {bmr})")
    print(f"Weight = {weight}, BMI = {bmi}")
    print("")

month = round(week*7/30, 2)

print(f"It will take almost {week*7} days for you to gain {goal-starting_weight} kg.")
print(f"Your BMI will be {bmi}.")

if month < 1:
    print("It will take less than a month to achieve your goal.")

elif 1 >= month < 2:
    print("You will achieve your goal almost in a month")

elif month >= 2:
    print(f"It will take {month} months to achieve your goal.")