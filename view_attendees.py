from data import events


# Displays the registered attendees for each available event
def view_attendee_lists():
    print("\n--- Attendee Lists ---")
 # Checks whether any events are available
    if len(events) == 0:
        print("No events are available.")
        return
# Goes through each event
    for event in events:
        print("\nEvent:", event["name"])

# Checks whether anyone has registered for the event
        if len(event["attendees"]) == 0:
            print("No attendees registered.")
        else:
            # Displays every registered attendee
            for attendee in event["attendees"]:
                print("-", attendee)







