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
print("Congratulations " + playerName + " you are an alpha tester!")
time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')
print('Incoming transmission', end='', flush=True)
time.sleep(2)
print(".", end='', flush=True)
time.sleep(2)
print(".", end='', flush=True)
time.sleep(2)
print(".", end='', flush=True)
time.sleep(2)


print("\nDeepVein corporation: Welcome to DeepVein, " + playerName + "!")
time.sleep(1)
print("""We are delighted that you have chosen to work for the galaxy’s most profitable mining corporation to date! 
Your duties are as follows: Deliver materials to our new mining operation on [insert planet name], perform any 
maintenance that may be required, and return to headquarters with the processed ores that have been stored in the 
depository.\n""")
time.sleep(1)
print("We are looking forward to working with you!\n")

wait = input("Press any key to continue.")