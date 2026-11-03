print("-" * 10 , "jadval zarb" , "-" * 10 )
while True :
    user_selection = input ("please enter your number :\n> enter skip for exit\n>")
    if user_selection == "skip" :
        break
    elif user_selection .isdigit () :
        for i in range (1 , 10) :
            user_selection = int (user_selection)
            print(f"{user_selection} * {i} = {user_selection * i}")
