from register_attendees import register_attendees

events = [
    {
        "name": "Painting Workshop",
        "date": "2026-09-12",
        "event_type": "Workshop",
        "capacity": 10,
        "attendees": ["Quad Azizi", "Bahaand Wardak"]
    },
    {
        "name": "7-a-side Football",
        "date": "2026-09-20",
        "event_type": "Sports",
        "capacity": 14,
        "attendees": ["Quresh Alshammari"]
    },
    {
        "name": "Charity Bake Sale",
        "date": "2026-10-01",
        "event_type": "Fundraiser",
        "capacity": 30,
        "attendees": ["Luke Parry"]
    }
]

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
        print("\n--- Available Events ---")
        for event in events:
            spaces_left = event["capacity"] - len(event["attendees"])
            print(f"{event['name']} ({event['event_type']})")
            print(f"   Date: {event['date']}")
            print(f"   Capacity: {len(event['attendees'])}/{event['capacity']} ({spaces_left} spaces left)")
    elif choice == "2":
        register_attendees(events)
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
