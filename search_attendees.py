from data import events

def search_attendees():
    attendees = []
    for event in events:
        for attendee in event["attendees"]:
            attendees.append(attendee)

    while True:
        attendee_searched = input('Search for an attendee by name (Enter N to exit): ').lower()
        if attendee_searched.strip() == 'n':
            return
        if attendee_searched.strip() == '':
            print('Please enter an attendee name.')
            continue
        searched_names = attendee_searched.split()
        found = False

        for attendee in attendees:
            split_attendee = attendee.lower().split()
            matches = 0

            for searched_name in searched_names:
                if searched_name in split_attendee:
                    matches += 1
            if len(searched_names) == matches:
                print(attendee)
                found = True
        if found == False:
            print('No attendee found')

