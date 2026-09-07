# Displays the registered attendees for each available event
def view_attendee_lists(events):
    print("\n--- Attendee Lists ---")

 # Checks whether any events are available
    if len(events) == 0:
        print("No events are available.")
        return
 # Goes through each event in the list
    for event in events:
        print("\nEvent:", event["name"])

 # Checks whether the event has any registered attendees
        if len(event["attendees"]) == 0:
            print("No attendees registered.")
        else:
 # Displays each attendee registered for the event
            for attendee in event["attendees"]:
                print("-", attendee)