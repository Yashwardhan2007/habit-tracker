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
tracker = Tracker()
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
