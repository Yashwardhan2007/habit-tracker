from datetime import date, timedelta
from habit import Habit

reading = Habit("Read 20 Pages")
today = date.today()

reading.mark_done(today)
reading.mark_done(today)

print(reading.is_done_on(today))
print (reading.is_done_on(today - timedelta(days=1)))
print(len(reading.completed_days))