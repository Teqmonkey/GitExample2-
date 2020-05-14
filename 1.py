# ---------------------1--testing ionlky -----------------------------------
#Learning DayTime
# INSTRUCTIONS: https://github.com/DJF3/Webex-Teams-Flask-oAuth/

from datetime import datetime
from datetime import date

today = datetime.today()2
today1 = date.today()

print(today1)

print(today1.year)


print(today)


christmas = date(2020,12,25)
print(christmas)

left = (christmas - today1).days
print(left)

if christmas is not today1:
    print("Sorry there are still " + str(left) + " untill Christams!.")
else:
    print("Yay its christmas")

