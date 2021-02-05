import msvcrt
import time
import random
from datetime import date
from datetime import datetime

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[100m'
    UNDERLINE = '\033[4m'


now = datetime.now()
ticketCode ="012654"
ticketGroup ="51465485/51488932"

ticketTotalCost = 45.0

ticketCurrentDrawNum =1121

ticketBoardset = []


today = date.today()
dayOfWeek = date.today()
strDayOfWeek = dayOfWeek.strftime('%A')
ticketPlayedOnDate = today.strftime("%d %B %Y")

date = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M:%S")

p=0

print("")

print("Number of draws: [2][3][4][5][6][7][8][9][10]")

# print(f"{bcolors.OKGREEN}Warning: No active frommets remain. Continue?{bcolors.ENDC}")

print(f"{bcolors.HEADER}--------------------------------------------{bcolors.ENDC}")
numberOfDraws = input(f"{bcolors.WARNING}Enter the number of draws you wish to play:{bcolors.ENDC}")


# print("You chose to play this ticket for: [" + numberOfDraws + "]draws!")

# confirmNumberOfDraws = input(f"{bcolors.WARNING}Press Enter to proceed | Esc for corrections:{bcolors.ENDC}")


# aborted = False

# for time_remaining in range(20,0,-1):
    
#     if msvcrt.kbhit() and msvcrt.getch() == chr(27).encode():
#         aborted = True
#         break

#     # print(str(time_remaining))       # so I can see loop is working
#     time.sleep(1) 

# if aborted:
#     print("Timed out")
# else:
#     print("...")

# time.sleep(5)  # to see result in command window before it disappears!


print(f"{bcolors.HEADER}--------------------------------------------{bcolors.ENDC}")
# print("Number of draws confirmed?" + confirmNumberOfDraws)
# print("--------------------------------------------")


ticketIsPowerBallPlus = input("PowerBall PLUS"+f"{bcolors.WARNING} (y/n)?:{bcolors.ENDC}")

while((ticketIsPowerBallPlus != 'y') and (ticketIsPowerBallPlus != 'n')):
    # print("Please reply with 'y' or 'n'") 
    ticketIsPowerBallPlus = input(f"{bcolors.WARNING}! Please reply with 'y' or 'n'...:{bcolors.ENDC}")

    if ticketIsPowerBallPlus == 'y':
        # ticketIsPowerBallPlus = "YES"
        break
    elif ticketIsPowerBallPlus == 'n':
        # ticketIsPowerBallPlus = "NO"
        break
    else:
        continue
    
if ticketIsPowerBallPlus == 'y':
    ticketIsPowerBallPlus = "YES"
elif ticketIsPowerBallPlus == 'n':
    ticketIsPowerBallPlus = "NO"

print(f"{bcolors.HEADER}--------------------------------------------{bcolors.ENDC}")
print("")
print(f"\t\t{bcolors.OKBLUE}{bcolors.UNDERLINE}{bcolors.BOLD}PowerBall{bcolors.ENDC}{bcolors.ENDC}{bcolors.ENDC}")
print("")

print("\t" + strDayOfWeek + ": ", ticketPlayedOnDate)

print("")
print("      First Draw: " + strDayOfWeek + " " + date)
print("       VALID RECEIPT FOR " ,numberOfDraws, " Draw(S)")


ticketlastDrawNum = ticketCurrentDrawNum + int(numberOfDraws)
print("\tFROM DRAW " , ticketCurrentDrawNum , " To " , ticketlastDrawNum)

print("\n\t   POWERBALL PLUS: " + ticketIsPowerBallPlus)
print("--------------------------------------------")



mainTicketTotalCost = ticketTotalCost * int(numberOfDraws)

print("--------------------------------------------")  
print("\t       Total :R", mainTicketTotalCost)
print("\t\t\t         Incl 15%VAT")  

print(ticketGroup + "\t\t      " + ticketCode)
print(date + "\t\t\t    " + time)
print("")

print("\t|||||||||||||||||||||||||")