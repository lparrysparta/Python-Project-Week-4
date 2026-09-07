from data import events

# shows all events and their parameters in a table
def show_events():
    print(f"{'Name':<35} | {'Date':<10} | {'Event Type':<25} | {'Spaces Left':<5}")
    print("-" * 74)
    for event in events:
        spaces_left = event['capacity'] - len(event['attendees'])
        print(f"{event['name']:<30} | {event['date']:<10} | {event['event_type']:<20} | {spaces_left:<5}")

# allows the user to book an event using their first and last name
def book_event():
    event_name = input("Please enter the name of the event you want to book: ")
    event = {}
    for e in events:
        if e['name'].lower() == event_name.lower():
            event = e
    if not event_full(event['attendees'], event['capacity']):
        name = get_attendee_name()
        if not already_registered(name, event['attendees']):
            event['attendees'].append(name)
            print("You have successfully registered to the " + event['name'] + ".")
        else:
            print("You are already registered. You cannot register for the same event twice.")
    else:
        print("This event is at max capacity. Please try again later, or book another event.")
    if not event:
        print("Event not found.")
        return

def get_attendee_name():
    first_name = input("Please provide your first name: ")
    last_name = input("Please provide your last name: ")
    return str(first_name + last_name)

def event_full(attendees, event_capacity):
    return len(attendees) >= event_capacity

def already_registered(attendee_name, attendees):
    return attendee_name in attendees

# def add_in_bulk(attendees_to_add, attendees):

def register_attendees():
    show_events()
    book_event()


# def main(events):
#     show_events()
#     book_event()

# if __name__ == "__main__":
#     main()















































