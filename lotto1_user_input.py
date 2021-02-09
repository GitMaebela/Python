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

print(f"{bcolors.OKCYAN}Number of draws: [2][3][4][5][6][7][8][9][10]{bcolors.ENDC}")

# print(f"{bcolors.OKGREEN}Warning: No active frommets remain. Continue?{bcolors.ENDC}")

print(f"{bcolors.HEADER}--------------------------------------------{bcolors.ENDC}")
numberOfDraws = int(input(f"{bcolors.WARNING}Enter the number of draws you wish to play:{bcolors.ENDC}"))


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

board = "A"

print(f"\t\t{bcolors.BOLD} Board " + f"{bcolors.ENDC}")
print(f"\t\t{bcolors.BOLD}   "+ board +"   "+ f"{bcolors.ENDC}")
isBoardQuickPlay = input("Quick Pick"+f"{bcolors.WARNING} (y/n)?:{bcolors.ENDC}")
isBoardCancelled = False
print("")
if isBoardQuickPlay == 'y':
    print("Board "+ board + " numbers will be generated for you!")
elif isBoardQuickPlay == 'n':
    print(f"{bcolors.OKCYAN}[1 ][2 ][3 ][4 ][5 ][6 ][7 ][8 ][9 ][10]{bcolors.ENDC}")
    print(f"{bcolors.OKCYAN}[11][12][13][14][15][16][17][18][19][20]{bcolors.ENDC}")
    print(f"{bcolors.OKCYAN}[21][22][23][24][25][26][27][28][29][30]{bcolors.ENDC}")
    print(f"{bcolors.OKCYAN}[31][32][33][34][35][36][37][38][39][40]{bcolors.ENDC}")
    print(f"{bcolors.OKCYAN}[41][42][43][44][45][46][47][48][49][50]{bcolors.ENDC}")
    manualChosen5Numbers = input(f"{bcolors.WARNING}Choose 5 numbers{bcolors.ENDC}" + f"{bcolors.HEADER}, comma separated:{bcolors.ENDC} ")
    
    print(f"{bcolors.OKCYAN}\t    [1 ][2 ][3 ][4 ]{bcolors.ENDC}")
    print(f"{bcolors.OKCYAN}\t[5 ][6 ][7 ][8 ][9 ][10]{bcolors.ENDC}")
    print(f"{bcolors.OKCYAN}\t[11][12][13][14][15][16]{bcolors.ENDC}")
    print(f"{bcolors.OKCYAN}\t    [17][18][19][20]{bcolors.ENDC}")
    manualChosen1PowerBall = input(f"{bcolors.WARNING}Choose 1 PowerBall: {bcolors.ENDC}")

    cancelBoard = input(f"{bcolors.HEADER}CANCEL BOARD?{bcolors.ENDC}"+f"{bcolors.WARNING} (y/n)?:{bcolors.ENDC}")
    
    if cancelBoard == 'y':
        isBoardCancelled = True
        print("Board " + board + " is cancelled!") 
    elif cancelBoard == 'n':
        isBoardCancelled = False
        print("Board " + board + " is successfully entered!") 
        print(manualChosen5Numbers +" | " + manualChosen1PowerBall)

print(f"{bcolors.HEADER}--------------------------------------------{bcolors.ENDC}")

print("")
print(f"\t{bcolors.BOLD}\t              \t{bcolors.ENDC}")
print(f"\t{bcolors.BOLD}\t PowerBall    \t{bcolors.ENDC}")
print(f"\t{bcolors.BOLD}\t              \t{bcolors.ENDC}")
print("")

print("\t" + strDayOfWeek + ": ", ticketPlayedOnDate)

print("")
# print("      First Draw: " + strDayOfWeek + " " + date)
print("       VALID RECEIPT FOR " ,numberOfDraws, " Draw(S)")

numberOfDraws -= 1

ticketlastDrawNum = ticketCurrentDrawNum + int(numberOfDraws)
print("\tFROM DRAW " , ticketCurrentDrawNum , " To " , ticketlastDrawNum)

print("\n\t   POWERBALL PLUS: " + ticketIsPowerBallPlus)
print("--------------------------------------------")

# board = ["A", "B", "C", "D", "E", "F"]
board = ["A", "B"]

length = len(board)  

for i in range(length):
    boardPowerBall = random.randrange(1, 21)
    str(boardPowerBall)
    # print("     ",board[i],"1(05): # # # # # ",board[i],"2(01):",format(boardPowerBall, '02d'))

    if isBoardQuickPlay == 'y':
        for q in range(1):
            while p < 5:
                p +=1
                randNum=random.randrange(1, 51)

                ticketBoardset.append(randNum)


                ticketBoardset.sort()

                strRandNum = str(randNum)

                # print(strRandNum + "   ",end='')

            if p == 5:
                p=0

            # print('   Std:', ticketBoardset," QP")
            
            ticketBoardset = list()
                
        # print("     ",board[i],"1(05): # # # # # ",board[i],"2(01):",format(boardPowerBall, '02d'))



mainTicketTotalCost = ticketTotalCost * int(numberOfDraws) * (numberOfDraws +1)

print("--------------------------------------------")  
print("\t       Total :R", mainTicketTotalCost)
print("\t\t\t         Incl 15%VAT")  

print(ticketGroup + "\t\t      " + ticketCode)
print(date + "\t\t\t    " + time)
print("")

print("\t|||||||||||||||||||||||||")