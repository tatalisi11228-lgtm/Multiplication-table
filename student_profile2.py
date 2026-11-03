name = input("Name and Family-name: ")
age = int(input("Age: "))
major = input("Major: ")
grade = float(input("Grade Point Average: "))

if grade > 20 or grade < 0:
    print("> Please enter a number between 0 to 20 ")
else:
    if grade >= 18:
        print("> Your grade is perfect")
    elif grade >= 12 and grade < 18:
        print("> Your grade is good")
    else:
        print("> You are on probation\n")

if age >= 18:
    print(f"> {name} is a collegian")
elif age < 18:
    print(f"> {name} is a student")
