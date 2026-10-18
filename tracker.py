from datetime import date
from habit import Habit
class Tracker:
    def __init__(self):
        self.habits : dict[str, Habit] = {}

    def add_Habit(self,name:str) -> Habit:
        """Create a new Habit. Names are case-insensitive and must be unique."""
        clean = name.strip()
        if not clean :
            raise ValueError("Habit name cannot be empty.")
        key = clean.lower()
        if key in self.habits:
            raise ValueError(f"Habit '{clean}' already exists.")
        habit = Habit(clean)
        self.habits[key] = habit
        return habit
    def find(self,name:str) -> Habit | None:
        """Return the habit with this name, or None if it doesn't exist."""
        return self.habits.get(name.strip().lower())

    def mark_done(self,name: str, day:date)-> bool:
        """Mark a habit as done. Returns False if the habit doesn't exist."""
        habit = self.find(name)
        if habit is None:
            return False
        habit.mark_done(day)
        return True

    def summary(self, today : date) -> list[str]:
        """One line per Habit with its current and longer streak."""
        lines = []
        for habit in self.habits.values():
            lines.append(
                f"{habit.name}: current streak {habit.current_streak(today)},"
                f"longest {habit.longest_streak()}"
            )
        return lines


