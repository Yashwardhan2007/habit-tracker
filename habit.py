from datetime import date

class Habit:
    def __init__(self, name: str):
        self.name = name
        self.completed_days : set[date] = set()

    def mark_done(self,day:date) -> None:
        """Record that the habit was done on this day."""
        self.completed_days.add(day)

    def is_done_on(self, day: date) -> bool:
        """Return True if the habit was done on this day... """
        return day in self.completed_days
    