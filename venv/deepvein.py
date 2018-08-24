#Project DeepVein Pre-Alpha Python 3.7.0 Test
# -*- coding: utf-8 -*-
import shelve, time, sys, os
def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def transmissionIncoming():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Incoming transmission', end='', flush=True)
    time.sleep(2)
    print(".", end='', flush=True)
    time.sleep(2)
    print(".", end='', flush=True)
    time.sleep(2)
    print(".\n\n", end='', flush=True)
    time.sleep(2)

def continueKey():
    wait = input("Press [ENTER] to continue...")

clearScreen()
print("Welcome to DeepVein\nThis is a Pre-Alpha Build.\n")
print("""
      ___           ___           ___           ___     
     /\  \         /\  \         /\  \         /\  \    
    /::\  \       /::\  \       /::\  \       /::\  \   
   /:/\:\  \     /:/\:\  \     /:/\:\  \     /:/\:\  \  
  /:/  \:\__\   /::\~\:\  \   /::\~\:\  \   /::\~\:\  \ 
 /:/__/ \:|__| /:/\:\ \:\__\ /:/\:\ \:\__\ /:/\:\ \:\__\\
 \:\  \ /:/  / \:\~\:\ \/__/ \:\~\:\ \/__/ \/__\:\/:/  /
  \:\  /:/  /   \:\ \:\__\    \:\ \:\__\        \::/  / 
   \:\/:/  /     \:\ \/__/     \:\ \/__/         \/__/  
    \::/__/       \:\__\        \:\__\                  
     ~~            \/__/         \/__/                  
      ___           ___                       ___     
     /\__\         /\  \          ___        /\__\    
    /:/  /        /::\  \        /\  \      /::|  |   
   /:/  /        /:/\:\  \       \:\  \    /:|:|  |   
  /:/__/  ___   /::\~\:\  \      /::\__\  /:/|:|  |__ 
  |:|  | /\__\ /:/\:\ \:\__\  __/:/\/__/ /:/ |:| /\__\\
  |:|  |/:/  / \:\~\:\ \/__/ /\/:/  /    \/__|:|/:/  /
  |:|__/:/  /   \:\ \:\__\   \::/__/         |:/:/  / 
   \::::/__/     \:\ \/__/    \:\__\         |::/  /  
    ~~~~          \:\__\       \/__/         /:/  /   
                   \/__/                     \/__/    \n""")
playerName = input("What is your name?\n")

while playerName == "":
    playerName = input("Please input a name:\n")

print("Congratulations " + playerName + " you are an alpha tester!")
time.sleep(2)


transmissionIncoming()

print("DeepVein corporation: Welcome to DeepVein, " + playerName + "!")
time.sleep(1)
print("""
____________________________________________________________________________________________________________________
|We are delighted that you have chosen to work for the galaxy’s most profitable mining corporation to date!         | 
|Your duties are as follows: Deliver materials to our new mining operation on XR-2521, perform any                  | 
|maintenance that may be required, and return to headquarters with the processed ores that have been stored in the  |
|depository.                                                                                                        |
-------------------------------------------------------------------------------------------------------------------- """)
time.sleep(1)
print("We are looking forward to working with you!\n")

continueKey()

clearScreen()
time.sleep(1)
print("""
Shortly after receiving this message you excitedly pack and prepare for your first voyage with the DeepVein Corporation.
You are directed to a shipyard and shown your brand new ship! Before long, you are waving goodbye to your home planet,
speeding towards adventure. The journey to XR-2521 takes several months,
even with DeepVein’s cutting edge technology; however, you spend this time in bliss,
cryogenically frozen in your very own cryo pod. 

You finally awaken to the sound of yet another transmission. 
""")


continueKey()

transmissionIncoming()

print("DeepVein corporation: Congratulations " + playerName + "!")
time.sleep(1)
print("""
______________________________________________________________________________________________________________________
|Congratulations, """ + playerName + """ you have arrived at XR-2521!                                                                    |
|You will be delighted know that you are the very first human representative to visit.                                |
|As a thank you for your dedicated time we would like you to give XR-2521 a more proper name.                         |
|Please respond with your desired choice and we will update our data systems.                                         |
----------------------------------------------------------------------------------------------------------------------
""")
time.sleep(1)
print("Thank you for working with DeepVein!\n")

planetName = input("Please name the planet: ")

while planetName == "":
    planetName = input("Please input a valid name for the planet:\n")

clearScreen()
time.sleep(1)
print("""
Still groggy from your slumber, you begin to feel the ship around you tremble.
Looking out the viewscreen in the cockpit, you see that you are now breaching the deep purple outer
atmosphere of the newly christened """ + planetName + """.
""")

continueKey()
clearScreen()

time.sleep(1)
print("""
You don your issued EVA suit and prepare your equipment for your first day on the job.
As you wait for your ship to dock with the materials depository on the ground you
hear another blip on the communications console.
""")
continueKey()

transmissionIncoming()
print("DeepVein Corporation: You have arrived!\n")
time.sleep(1.5)
print("Below are your duties for the day. Please report back to the ship when all are completed, thank you.\n")
time.sleep(1)
print("""
 ____________________________________________________________________________________________________________________
|-Access the depository and transit lines.                                                                           | 
|-Visit both mining operations at the mountains to the east and west.                                                |
|-Confirm that all solar panels are operating efficiently and that there are no breaks in the power supply.          |
 --------------------------------------------------------------------------------------------------------------------
""")
continueKey()
clearScreen()
time.sleep(1)

print("""
The ship gives one last shudder as it finishes its docking process and the lights in the cockpit shift
to a soft green hue, signifying that it is safe to disembark.
You enter the airlock and cycle it, depressurizing the ship and revealing the outside world.
Directly in front of you lies the massive depository building where the processed materials are stored and prepared
for transit back to DeepVein Headquarters. Running east and west from the building are two roads beaten into the dust
by large transit vehicles, bristling with solar panels and sensor arrays. You see a couple of these in the distance
heading towards the depository. Beyond the depository lies the solar field where hundreds more solar panels lie
in the green-gray dust. The day is yours. What duty would you like to accomplish first?\n 
""")
time.sleep(1)
print("""
[a] - Access the depository and transit lines.
[b] - Visit both mining operations at the mountains to the east and west.
[c] - Confirm that all solar panels are operating efficiently and that there are no breaks in the power supply.\n""")

while True:
    decision1 = input("What would you like to do? ")
    if decision1 not in ("a", "b", "c", "e"):
        print("Not a valid action.")
    else:
        break

if decision1 == "a":
    clearScreen()
    time.sleep(1)
    print("""You step off the ship’s gangplank and into the dirt, approaching the depository. 
The building looms over you.""")

if decision1 == "b":
    clearScreen()
    time.sleep(1)
    print("""You step into the dirt of """ + planetName + """ and begin making your way towards a small
refueling depot where you know you can hitch a ride to either of the mountains on the transit vehicles.""")

if decision1 == "c":
    clearScreen()
    time.sleep(1)
    print("""You begin to make your way past the imposing depository and into the solar fields to access
any damage or dust coverage on the solar panels.""")

if decision1 == "e":
    clearScreen()
    time.sleep(2)
    print("""You turn around, back into [insert ship name] and recycle the airlock.
Ignoring the comms console you power up the ship and return to your blissful slumber in the cryo pod.
When you awake you receive one last message.""")
    transmissionIncoming()
    print("DeepVein corporation: You’re employment with the Deepvien corporation has been terminated.\n")
    time.sleep(1)
    print("""
 ___________________________________________________________________________________________________________________
|Your employment with the DeepVein Corporation has been terminated.                                                 |    
 ------------------------------------------------------------------------------------------------------------------- 
 """)
    time.sleep(1)


continueKey()