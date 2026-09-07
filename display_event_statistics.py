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

total_registrations = 0
total_capacity = 0
for event in events:
    total_registrations += len(event["attendees"])
    total_capacity += (event["capacity"])
total_spaces_remaining = total_capacity - total_registrations

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