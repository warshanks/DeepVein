import shelve, time, sys, os

if os.name == 'nt':
    os.system("mode con cols=120 lines=50")

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def transmissionIncoming():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Incoming transmission', end='', flush=True)
    time.sleep(1)
    print(".", end='', flush=True)
    time.sleep(1)
    print(".", end='', flush=True)
    time.sleep(1)
    print(".\n\n", end='', flush=True)
    time.sleep(1)

def continueKey():
    wait = input("Press [ENTER] to continue...")

def slowPrint(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)


planetName = "testingplanet"
playerName = "testingplayer"

#def slowPrint(s):
    #for c in s:
        #sys.stdout.write(c)
        #sys.stdout.flush()
        #time.sleep(0.01)

#slowPrint("This is a test")


#if 1 == 1:
   # check1 = 1


#if 1 != 1:
  #  check2 = 1

#if 1 == 1:
 #   check3 = 1


#if check1 + check2 + check3 >= 2:
 #   print("Pass check")
#else: print("Fail check")
choiceA = "[a] - Access the depository and transit lines.\n"
choiceB = "[b] - Visit both mining operations at the mountains to the east and west.\n"
choiceC = "[c] - Confirm that all solar panels are operating efficiently and that there are no breaks in the power supply.\n"
i = 0
while i < 2:

    print(choiceA + choiceB + choiceC)

    while True:
        decision1 = input("What would you like to do? ")
        if decision1 not in ("a", "b", "c", "e"):
            print("Not a valid action.")
        else:
            break

    if decision1 == "a":
        i += 1
        clearScreen()
        time.sleep(1)
        print("""You step off the ship’s gangplank and into the dirt, approaching the depository. 
The building looms over you.""")
        choiceA = ""
        continueKey()
        clearScreen()

    if decision1 == "b":
        i += 1
        clearScreen()
        time.sleep(1)
        print("""You step into the dirt of """ + planetName + """ and begin making your way towards a small
refueling depot where you know you can hitch a ride to either of the mountains on the transit vehicles.""")
        choiceB = ""
        continueKey()
        clearScreen()

    if decision1 == "c":
        i += 1
        clearScreen()
        time.sleep(1)
        print("""You begin to make your way past the imposing depository and into the solar fields to access
any damage or dust coverage on the solar panels.""")
        choiceC = ""
        continueKey()
        clearScreen()

print("Loop complete", i)
