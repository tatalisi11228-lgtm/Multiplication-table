print("============= bank acount =============")

while True:
    username = input("> Enter your username: ")
    if username == "hamid8134":
        break
    print(f"{username} is incorrect")

while True:
    password = input("> Enter your password: ")
    if password == "Hamid@123456":
        break
    print(f"{password} is incorrect")

print("\n========== acount balance ==========")
print("You have 0$ in your acount")
account = 0
while True:
    edit = input(
        "> Type 'I' to increase or 'D' to decrease amount of account(Press enter to see your account balance / q to exit): "
    )
    if edit == "":
        print(f"You have {account}$")
    elif edit == "q":
                break
    elif edit == "I":
        increase = input(
            "> How much money would like to put in your bank account?(Press enter to see your account balance / q to exit) "
        )
        if increase == "":
            print(f"You have {account}$")
        elif increase == "q":
            break
        elif increase.isdigit():
            account += int(increase)
        else:
            print("Please enter a valid positive number")
    elif edit == "D":
        decrease = input(
            "> How much money would you like to withraw from the bank?(Press enter to see your account balance / q to exit) "
        )
        if decrease == "":
            print(f"You have {account}$")
        elif decrease == "q":
            break
        elif decrease.isdigit():
            account -= int(decrease)
        else:
            print("Please enter a valid positive number")
    else:
        print("Please enter 'I' or 'D' or 'q' or press enter to exit")
