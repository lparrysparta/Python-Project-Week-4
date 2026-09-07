attendees = ['John Smith', 'Lisa Turner', 'Jane Doe', 'John Doe', 'John Quincy Adams', 'Tony Adams']

while True:
    attendee_searched = input('Search for an attendee by name: ').lower()
    if attendee_searched.strip() == '':
        print('Please enter an attendee name.')
        continue
    searched_names = attendee_searched.split()

    for attendee in attendees:
        split_attendee = attendee.lower().split()
        matches = 0

        for searched_name in searched_names:
            if searched_name in split_attendee:
                matches += 1

        if len(searched_names) == matches:
            print(attendee)

