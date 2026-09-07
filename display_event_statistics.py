from data import events

total_registrations = 0
total_capacity = 0
for event in events:
    total_registrations += len(event["attendees"])
    total_capacity += (event["capacity"])
total_spaces_remaining = total_capacity - total_registrations

def display_event_statistics():
    print('')
    print("Overall Event Statistics")
    print(f"Total events: {len(events)}")
    print(f"Total capacity: {total_capacity}")
    print(f"Total registrations: {total_registrations}")
    print(f"Total spaces remaining: {total_spaces_remaining}")
    print('')

    for event in events:
        print(f"{event["name"]} Statistics")
        print(f"Maximum capacity: {event["capacity"]}")
        print(f"Registered: {len(event["attendees"])}")
        print(f"Spaces remaining: {event["capacity"] - len(event['attendees'])}")
        print('')