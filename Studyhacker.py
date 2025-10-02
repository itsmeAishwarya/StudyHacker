# Simple Study Tracker
# You can add your study sessions, see all sessions, and get total hours per subject.

import json      # to save and load data from a file
import os        # to check if file exists
from datetime import datetime  # to get current date and time

# Name of the file where we will store study data
FILENAME = "study_data.json"

# Step 1: Load old data if it exists, otherwise start empty
if os.path.exists(FILENAME):
    with open(FILENAME, "r") as file:
        study_data = json.load(file)
else:
    study_data = []

# Function to add a new study session
def add_session():
    # Ask user for subject and hours studied
    subject = input("Enter subject/topic: ")
    hours = float(input("Enter hours studied (e.g., 1.5): "))
    
    # Get the current date and time
    date = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # Make a dictionary for this session
    session = {"subject": subject, "hours": hours, "date": date}
    
    # Add the session to our list
    study_data.append(session)
    
    # Save the list back to the file
    with open(FILENAME, "w") as file:
        json.dump(study_data, file, indent=4)
    
    print("✅ Study session added!\n")

# Function to view all study sessions
def view_sessions():
    if not study_data:
        print("No study sessions recorded yet.\n")
        return
    print("📚 Your study sessions:")
    for i, session in enumerate(study_data, 1):
        print(f"{i}. {session['date']} - {session['subject']} : {session['hours']} hours")
    print()

# Function to show total hours per subject
def summary():
    if not study_data:
        print("No study data to summarize.\n")
        return
    
    totals = {}  # Dictionary to store total hours per subject
    for session in study_data:
        # If subject already in totals, add hours; otherwise, start with current hours
        if session['subject'] in totals:
            totals[session['subject']] += session['hours']
        else:
            totals[session['subject']] = session['hours']
    
    print("📊 Total hours per subject:")
    for subject, hours in totals.items():
        print(f"{subject}: {hours} hours")
    print()

# Main program loop
def main():
    while True:
        print("=== Study Tracker Menu ===")
        print("1. Add study session")
        print("2. View all sessions")
        print("3. View summary")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")
        print()
        
        if choice == "1":
            add_session()
        elif choice == "2":
            view_sessions()
        elif choice == "3":
            summary()
        elif choice == "4":
            print("Goodbye! Keep studying! 💪")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

# Start the program
if __name__ == "__main__":
    main()
