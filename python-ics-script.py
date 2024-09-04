from ics import Calendar, Event 
from dateutil import parser as date_parser
from datetime import datetime
import os

def create_ics_file(title,description,deadline,location,output_file):
    #create the calendar
    cal=Calendar()

    #create an event
    event=Event()
    event.name=title
    event.description=description
    event.begin=deadline
    event.location=location

    #add event to the calendar
    cal.events.add(event)

    #write the event to an .ics file
    with open(output_file, 'w') as f:
        f.writelines(cal)

    print(f"ICS file created: {output_file}")

def main():
    #collect the input from the user
    title = input("Enter the title:")
    description = input("Enter a description:")
    deadline = input("Deadline in 'YYYY-MM-DD HH:MM' format:")
    location = input("Optional Location:")
    output_file = input("Enter output file in 'name.ics' format:")

    #convert the deadline input into into a date time object
    try:
        deadline_dt= date_parser.parse(deadline)
        deadline_dt = deadline_dt.astimezone()
    except ValueError:
        print ("Invalid date format 'YYYY-MM-DD HH:MM'.")
        return
    
    create_ics_file(title,description,deadline_dt,location,output_file)

if __name__ == "__main__":
    main()