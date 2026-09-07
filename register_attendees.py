from menu import events

def show_events(events):
    print(f"{'ID':<4} | {'Name':<30} | {'Date':<10} | {'Location':<20} |{'Spaces Left':<5}")
    print("-" * 62)
    for event in events:
        spaces_left = event['capacity'] - len(event['attendees'])
        print(f"{event['id']:<4} | {event['name']:<30} | {event['date']:<10} | {event['location']:<20} | {spaces_left:<5}")

def book_event():
    event_name = input("Please enter the name of the event you want to book: ")
    event = {}
    for e in events:
        if e['name'] == event_name:
            event = e
    if not event_full(event['attendees'], event['capacity']):
        name = get_attendee_name
        if not already_registered(name, event['attendees']):
            # TO DO: edit this with full attendee record if necessary, may just use name though
            event['attendees'].append(name)
        else:
            print("You are already registered. You cannot register for the same event twice.")
    else:
        print("This event is at max capacity. Please try again later, or book another event.")

def get_attendee_name():
    first_name = input("Please provide your first name: ")
    last_name = input("Please provide your last name: ")
    return first_name, last_name

def event_full(attendees, event_capacity):
    return len(attendees) >= event_capacity

def already_registered(attendee_name, attendees):
    return attendee_name in attendees

# def add_in_bulk(attendees_to_add, attendees):

def main():
    show_events(events)
    book_event()




















































