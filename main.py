from data import events
from register_attendees import register_attendees
from search_attendees import search_attendees
from view_attendees import view_attendee_lists
from display_event_statistics import display_event_statistics
from menu import menu


while True:
    number = menu()

    if number == '2':
        register_attendees()

    if number == '3':
        view_attendee_lists()

    if number == '4':
        search_attendees()

    if number == '5':
        display_event_statistics()

    if number == '6':
        break