from datetime import date, timedelta

from habit import Habit
from tracker import Tracker

"""habit = Habit("Read 20 Pages")
today = date(2026, 10, 18)

for offset in [0,1,3,4,5,6]:
    habit.mark_done(today - timedelta(days = offset))

print(habit.current_streak(today))
print(habit.longest_streak())
print(habit.current_streak(today+timedelta(days=1)))
print(habit.current_streak(today+ timedelta(days=2)))
"""
"""tracker = Tracker()
today= date(2026, 10, 18)

tracker.add_Habit("Red 20 pages")
tracker.add_Habit("Gym")
tracker.add_Habit("Study Python")

for offset in [0,1,2]:
    tracker.mark_done("read 20 pages", today - timedelta(days=offset))
tracker.mark_done("Gym", today)
for line in tracker.summary(today):
    print(line)
print(tracker.mark_done("Swimming", today))

try:
    tracker.add_Habit("gym")
except ValueError as error:
    print("Error:", error)
"""

MENU = """
______ Habit Tracker_____
1. Add a Habit
2. Mark a habit as done today
3. Mark a habit as done on another date
4. Show streaks
0. QUIT!!!!
"""

def ask_date(prompt: str) -> date | None:
    """Ask for a date like 2026-10-18. Returns None if the input is invalid."""
    text = input(prompt).strip()
    try:
        return date.fromisoformat(text)
    except ValueError:
        print("Please use the format YYYY-MM-DD, for eg: 2026-10-18..")
        return None
def main()-> None:
    tracker = Tracker()

    while True:
        print(MENU)
        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = input ("Habit name: ")
            try:
                habit = tracker.add_Habit(name)
                print(f"Added '{habit.name}'.")
            except ValueError as error:
                print("Error:", error)

        elif choice == "2":
            name = input ("Which habit??? ")
            if tracker.mark_done(name, date.today()):
                print("No habit with that name.")
            else:
                print("No habit with that name.")#

        elif choice == "3":
            name = input("Which habit??? ")
            day = ask_date("Date (YYYY-MM-DD): ")
            if day is None:
                continue
            if day > date.today():
                print("That data is in the future...")
            elif tracker.mark_done(name, day):
                print(f"Marked as done on {day}...")
            else:
                print("No habit with that name...")

        elif choice == "4":
            lines = tracker.summary(date.today())
            if not lines:
                print("No habits yet. ")
            for line in lines :
                print(line)

        elif choice == "0":
            print("Bye!!!!! ")
            break

        else:
            print("Invalid Option, please choose 0-4... ")

if __name__ == "__main__":
    main()
