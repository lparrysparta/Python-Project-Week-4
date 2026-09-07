class RegisterAttendees:

    def show_events(self, events):
        print(f"{'ID':<4} | {'Name':<30} | {'Date':<10} | {'Location':<20} |{'Spaces Left':<5}")
        print("-" * 62)
        for event in events:
            spaces_left = event['capacity'] - len(event['attendees'])
            print(f"{event['id']:<4} | {event['name']:<30} | {event['date']:<10} | {event['location']:<20} | {spaces_left:<5}")

    def book_event(self):
        event_name = input("Please enter the name of the event you want to book: ")
        # TO DO: use view available events to obtain an event record for next step
        event = event_name.ViewAvailableEvents
        if not RegisterAttendees.event_full(event['attendees'], event['capacity']):
            name = RegisterAttendees.get_attendee_name
            if not RegisterAttendees.already_registered(name, event['attendees']):
                # TO DO: edit this with full attendee record if necessary, may just use name though
                event['attendees'].append(name)
            else:
                print("You are already registered. You cannot register for the same event twice.")
        else:
            print("This event is at max capacity. Please try again later, or book another event.")

    def get_attendee_name(self):
        first_name = input("Please provide your first name: ")
        last_name = input("Please provide your last name: ")
        return first_name, last_name

    def event_full(self, attendees, event_capacity):
        return len(attendees) >= event_capacity

    def already_registered(self, attendee_name, attendees):
        return attendee_name in attendees

    def add_in_bulk(self, attendees_to_add, attendees):

    def main(self):
        # TO DO: get event records to add as an argument for show_events
        RegisterAttendees.show_events()
        RegisterAttendees.book_event()




















































