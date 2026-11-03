name = input("name and family name: ")
student_number = input("student number: ")
major = input("major: ")
current_semester = input("current semester: ")
remaining_semester = input("remaining semester: ")

print(
    f" Your name is: {name}\n"
    f" Your student number is: {student_number}\n"
    f" You are studying {major}\n"
    f" You are in semester {current_semester}"
    )

if remaining_semester == "1":
    print(" You have 1 semester left")
else:
    print(f" You have {remaining_semester} semesters left")

