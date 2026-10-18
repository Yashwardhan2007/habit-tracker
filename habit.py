from datetime import date, timedelta

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

    def current_streak(self,today: date)->int:
        """Consecutive days ending today(or yesterday, if today isn't done yet)."""
        if today in self.completed_days:
            day=today
        elif today - timedelta(days=1) in self.completed_days:
            day = today - timedelta(days = 1)
        else:
            return 0
        streak = 0
        while day in self.completed_days:
            streak+=1
            day -= timedelta(days=1)
        return streak

    def longest_streak(self) -> int:
        """Longest run of consecutive days ever recorded."""
        longest = 0
        current = 0
        previous = None
        for day in sorted(self.completed_days):
            if previous is not None and day - previous == timedelta(days=1):
                current+= 1
            else:
                current = 1
            longest = max(longest, current)
            previous = day
        return longest