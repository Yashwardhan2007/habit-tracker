import json
from datetime import date
from pathlib import Path

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

    def save(self, path : Path) -> None:
        """Write all habits to a JSON file."""
        path.parent.mkdir(parents=True, exist_ok=True)
        data = [habit.to_dict() for habit in self.habits.values()]
        path.write_text(json.dumps(data, indent = 2), encoding = "utf-8")

    def load(self, path:Path) -> None:
        """Read habits from a JSON file. Does nothing if the file doesn't exist..."""
        if not path.exists():
            return
        data = json.loads(path.read_text(encoding = "utf-8"))
        for item in data:
            habit = Habit.from_dict(item)
            self.habits[habit.name.lower()] = habit
