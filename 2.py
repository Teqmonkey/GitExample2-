# ------------------------------------------------------------
#Learning DayTime
# INSTRUCTIONS: How much time left , we measure time left untill a specific task is met . 
# eg i can say i have 4 days and 10 hours before my next time off at work. Timedelat can only go up to 23hr and 59mins

from datetime import datetime
from datetime import timedelta

t = timedelta(days=4 , hours=10)
print(t.days)
print("The second left in 10 hours is: " + str(t.seconds))


eta = timedelta(hours=6)
print(eta)
today = datetime.today()

print(today)

now=today + eta
print(now)