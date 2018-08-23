#Project DeepVein Pre-Alpha Python 3.7.0 Test
# -*- coding: utf-8 -*-
import shelve, time, sys, os


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
    wait = input("Press any key to continue...")

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
Shortly after receiving this message you excitedly pack and prepare for your first voyage with the Deepvein Corporation.
You are directed to a shipyard and shown your brand new ship! Before long, you are waving goodbye to your home planet,
speeding towards adventure. The journey to XR-2521 takes several months,
even with DeepVein’s cutting edge technology; however, you spend this time in bliss,
cryogenically frozen in your very own cryo pod. 

You are finally awaken to the sound of yet another transmission. 
""")


continueKey()

transmissionIncoming()

print("DeepVein corporation: Congratulations " + playerName + "!")
time.sleep(1)
print("""
______________________________________________________________________________________________________________________
|Congratulations, """ + playerName + """ you have arrived at XR-2521!                                                                    |
|You will be delighted to be informed that you are the very first human representative to visit                       |
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
atmosphere of """ + planetName + """.
""")

continueKey()