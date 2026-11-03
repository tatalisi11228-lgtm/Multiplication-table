TOTAL_SEMESTERS = 8

name = input("Name and family name: ")

# I should confess that this part was a bit AI's assistant but, ــonlyــ till line 11.
# I totally know that wasn't necessary but, it would make the project more interesting.
while True:
    student_number = input("Student number (16 digits): ")
    if len(student_number) == 16 and student_number.isdigit():
        break
    print(f"Student number must be 16 digits - that was {len(student_number)} characters.")

major = input("Major: ")
current_semester = int(input("Current semester (1-8): "))
remaining_semesters = int(input("Remaining semesters: "))

if current_semester < 1 or current_semester > TOTAL_SEMESTERS:
    print(f"\nA semester number must be between 1 and {TOTAL_SEMESTERS}.")
else:
    if remaining_semesters == 1:
        remaining_line = "1 semester"
    else:
        remaining_line = f"{remaining_semesters} semesters"

    print(
        f"\n--- Student profile ---\n"
        f"Name             : {name}\n"
        f"Student number   : {student_number}\n"
        f"Major            : {major}\n"
        f"Current semester : {current_semester} of {TOTAL_SEMESTERS}\n"
        f"Remaining        : {remaining_line}"
    )
