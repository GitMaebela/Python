import random
from datetime import date

from datetime import datetime

now = datetime.now()
ticketCode="012654"
ticketGroup="51465485/51488932"
ticketTotalCost="45.00"
ticketBoardset = []
p=0

print("")
print("\t\tPowerBall")
print("")
today = date.today()

dayOfWeek = date.today()

strDayOfWeek = dayOfWeek.strftime('%A')

ticketPlayedOnDate = today.strftime("%d %B %Y")

print("\t" + strDayOfWeek + ": ", ticketPlayedOnDate)
print("\tPOWERBALL PLUS: ")
print("----------------------------------------")

for q in range(6):
    print("   A(5): ",end='')
    while p < 5:
        p +=1
        randNum=random.randrange(1, 51)

        ticketBoardset.append(randNum)

        ticketBoardset.sort()
        strRandNum=str(randNum)
        print(strRandNum + "   ",end='')
        
    if p == 5:
        print("\n",end='')
        p=0

    print('   Std:', ticketBoardset)
    
    ticketBoardset = list()

print("----------------------------------------")  
print("\t     Total :R" + ticketTotalCost)
print("\t\t\t     Incl 15%VAT")  

date = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M:%S")

print(ticketGroup + "\t\t  " + ticketCode)
print(date + "\t\t\t" + time)
print("")

print("\t|||||||||||||||||||||||||")