from datetime import date, timedelta

from habit import Habit

habit = Habit("Read 20 Pages")
today = date(2026, 10, 18)

for offset in [0,1,3,4,5,6]:
    habit.mark_done(today - timedelta(days = offset))

print(habit.current_streak(today))
print(habit.longest_streak())
print(habit.current_streak(today+timedelta(days=1)))
print(habit.current_streak(today+ timedelta(days=2)))