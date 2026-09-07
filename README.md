Community Event Management System

A group Python application that helps staff manage community events and attendee registrations through a command line menu.

GitHub repository

Objectives

Reduce reliance on paper forms and spreadsheets by providing one application for viewing events, registering attendees, checking attendee lists, searching names and displaying event statistics.

Features

View event names, dates, types, capacity and remaining spaces.

Register attendees, with capacity and duplicate name checks.

Display attendee lists for each event, including messages for empty lists.

Search attendees without case sensitivity and return to the menu by entering N.

Display overall and individual event statistics.

Exit the application.

The sample events are Painting Workshop, 7-a-side Football and Charity Bake Sale.

How the Application Works

The flowchart summarises navigation through the application. Options 1 to 5 correspond to the features listed above. Search remains active until the user enters N.

flowchart TD
    A[Start application] --> B[Display menu]
    B --> C{Menu choice}
    C -->|1 to 5| D[Run selected feature]
    C -->|6| I[Exit application]
    C -->|Invalid option| J[Display error message]
    D -->|Finish or leave feature| B
    J --> B

Team Contributions

Qudratulla: Available Events and Menu

Developed the event display in menu.py, showing each event's name, date, type, capacity and remaining spaces. The menu presents all six options and provides feedback when an invalid option is entered.

Luke: Attendee Registration

Developed register_attendees.py, allowing staff to select an event and enter an attendee's first and last names. Added checks for full events and exact duplicate names before adding a registration to the shared attendee list.

Qurash: View Attendee Lists

Developed view_attendees.py, which loops through the shared events and displays the registered attendees under each event name. Added messages for situations where no events are available or an event has no registered attendees.

Bahaand: Shared Data, Search and Statistics

Prepared the shared event records in data.py and developed search_attendees.py to find attendee names without case sensitivity, with feedback for blank entries and no matches. Developed display_event_statistics.py to present overall totals and individual event capacity, registration and remaining space figures.

The group combined the features into one application using shared event data.

Methodology and GitHub Collaboration

The application uses variables, lists, dictionaries, conditional statements, loops, functions and basic input/output. Event records are stored in a shared list in data.py.

Team members worked on individual feature branches and used descriptive commit messages. Pull requests were reviewed before integration into dev, with two approving reviews required by the group's workflow. Completed work was then merged into main.

Project Files

File

Purpose

main.py

Runs the application loop and calls feature functions

menu.py

Displays menu choices, lists events and handles invalid menu options

data.py

Stores sample events and attendee lists

register_attendees.py

Displays booking options and registers attendees

view_attendees.py

Displays each event's attendee list

search_attendees.py

Searches registered attendee names

display_event_statistics.py

Displays overall totals and individual event statistics

How to Run

Use Python 3.12 or later. The current statistics file uses f-string syntax that requires Python 3.12 or newer. No third party Python packages are required.

git clone https://github.com/lparrysparta/Python-Project-Week-4.git
cd Python-Project-Week-4
python3 main.py

Choose a menu option from 1 to 6. Run main.py to use the complete application.

Testing Checklist

Use this checklist to verify the application when making changes:

Check that event details and available spaces display correctly.

Register an attendee and confirm their name appears in the attendee list.

Search for an existing name, an unknown name and a blank entry.

Check registration behaviour for full events and duplicate names.

Compare statistics before and after registration.

Check invalid menu entries and exit using option 6.

Future Development

Add permanent file storage, improve registration validation and name formatting, recalculate overall statistics when requested, support cancellation and introduce automated tests. A graphical interface could make the application easier for staff to use.
