def add_todo_item():
    item = input("Enter your new To-do item: ")
    with open("to_do.txt", "a") as file:
        file.write(item + "\n")
    print("To-Do item added successfully.\n")


def list_todo_item():
    try:
        with open("to_do.txt", "r") as file:
            item = file.readlines()
            if not item:
                print("Your To-Do list is empty.\n")
            else:
                print("\nYour To-Do list: ")
                for item in item:
                    print(item.strip())
                print()
    except FileNotFoundError:
        print("No To-Do list found yet.\n")

while True:
    choice = input("Do you want to add a new To-Do item? ( y / n ) or type 'exit':").lower()

    if choice == "exit":
        print("Thank you for using the To-Do program, come back again soon")
        break

    if choice == "y":
        add_todo_item()

    elif choice == "n":
        read_choice = input("Do you want to list your To-Do item? ( y / n ): ").lower()

        if read_choice == "y":
            list_todo_item()

    else:
        print("Invalid choice, please try again.\n")