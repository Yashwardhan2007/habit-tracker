from datetime import date
from pathlib import Path

from habit import Habit
from tracker import Tracker

DATA_FILE = Path("data/habits.json")

MENU = """
________ HABIT TRACKER _______
1. Add a Habit :
2. Mark a Habit as done today : 
3. Mark a Habit as done on another date : 
4. Show streaks :
0. QUITT!!!!
"""

def ask_date(prompt : str) -> date | None:
    """Ask for a date like 2026-10-18. Return None if the input is invalid."""
    text = input(prompt).strip()
    try:
        return date.fromisoformat(text)
    except ValueError:
        print("Please use the format YYYY-MM-DD, for eg: 2026-10-18.")
        return None
def main() -> None:
    tracker = Tracker()
    tracker.load(DATA_FILE)

    while True:
        print(MENU)
        choice = input("Choose an option : ").strip()

        if choice == "1":
            name = input("Habit name: ")
            try:
                habit = tracker.add_Habit(name)
                tracker.save(DATA_FILE)
                print(f"Added '{habit.name}'.")
            except ValueError as error:
                print("Error:", error)

        elif choice == "2":
            name = input("Which habit? ")
            if tracker.mark_done(name, date.today()):
                tracker.save(DATA_FILE)
                print("Marked as done today.")
            else:
                print("No habit with that name.")

        elif choice == "3":
            name = input("Which habit? ")
            day = ask_date("Date (YYYY-MM-DD): ")
            if day is None:
                continue
            if day > date.today():
                print("That date is in the future.")
            elif tracker.mark_done(name, day):
                tracker.save(DATA_FILE)
                print(f"Marked as done on {day}.")
            else:
                print("No habit with that name.")

        elif choice == "4":
            lines = tracker.summary(date.today())
            if not lines:
                print("No habits yet.")
            for line in lines:
                print(line)

        elif choice == "0":
            print("Bye!")
            break

        else:
            print("Invalid option, please choose 0-4.")


if __name__ == "__main__":
    main()