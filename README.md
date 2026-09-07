# Menu Code



running = True

while running:
    print("\n===== Community Event Management System =====")
    print("1. View available events")
    print("2. Register an attendee")
    print("3. View attendee list")
    print("4. Search for an attendee")
    print("5. Display event statistics")
    print("6. Add a new event (bonus)")
    print("7. Exit")

    choice = input("Choose an option (1-7): ")

    if choice == "1":
        print("You chose: View available events")
    elif choice == "2":
        print("You chose: Register an attendee")
    elif choice == "3":
        print("You chose: View attendee list")
    elif choice == "4":
        print("You chose: Search for an attendee")
    elif choice == "5":
        print("You chose: Display event statistics")
    elif choice == "6":
        print("You chose: Add a new event")
    elif choice == "7":
        print("Goodbye!")
        running = False
    else:
        print("Invalid option -- please choose a number between 1 and 7.")
