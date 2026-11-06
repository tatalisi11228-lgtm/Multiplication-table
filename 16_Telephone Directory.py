contacts = {}
while True:
    name = input(
        "> Enter your contact(press Enter to see your contacts): ").strip().lower()
    if not name:
        if not contacts:
            print("\nYou haven't added any contact yet\n")
            continue
        break

    number = input(f"{name}: ").strip()
    if not number:
        print("No number entered, try again.")
        continue

    contacts[name] = number

print("\n\nAll contacts:\n")
for name, number in contacts.items():
    print(f"{name} = {number}")

while True:
    search = input(
        "> Who are you searching for(Press enter to stop)? ").strip().lower()
    if not search:
        print("Stopped")
        break

    if search in contacts:
        print(f"{search}: {contacts[search]}")
    else:
        add = input(
            f"Not found. Add {search} to your contacts? (y/n) ").strip().lower()
        while add not in ["y", "n"]:
            print("Invalid input, please enter 'y' or 'n'.")
            add = input(
                f"Not found. Add {search} to your contacts? (y/n) ").strip().lower()

        if add == "y":
            number = input("> Enter your new contact's number: ").strip()
            while not number:
                print("Nothing entered, try again.")
                number = input("> Enter your new contact's number: ").strip()

            contacts[search] = number
            print(f"Saved {search}.")

        else:
            print('\n', "=" * 10, 'Alright', "=" * 10)
            print("\nAll contacts:\n")
            for name, number in contacts.items():
                print(f"{name} = {number}")
            break
