from datetime import date
import datetime


d = datetime.date(2021, 2, 10)
# while d.weekday() != 1: #0 for monday
#     d += datetime.timedelta(days=5)

today = date.today()
print("Today is: ", today, today.strftime('%A'))

print("The ticket is played on: ", d,d.strftime('%A'))

if d.weekday()  <= 1: #0 for monday
    print("Next draw is on: Tuesday")
elif (d.weekday() > 1) and (d.weekday() <= 4):
    print("Next draw is: Friday")
else:
     print("Next draw is on: Tuesday")   
    

# strNextDrawDayOfWeek = d.strftime('%A')
# print(d)
# print(strNextDrawDayOfWeek)