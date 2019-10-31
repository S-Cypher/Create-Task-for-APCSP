import tkinter as tk
from time import sleep
import os

os.system('cls')
print("Press 'Start' to start the adventure!")

sword = False
monster_killed = False

def story_start():
    os.system('cls')
    print("You're exploring a forest when you come across a cave.")
    sleep(0.8)
    print("You've been traveling for a long time and you're tired but, the cave intrigues you.")
    sleep(0.8)
    print("Do you travel in the cave or make a campsite?")
    choice1.configure(text="Cave",command=cave)
    choice2.configure(text="Campsite",command=campsite)

    
def cave():
    os.system('cls')
    print("You chose to explore the cave.")
    sleep(0.8)
    print("You come across a sword on the ground")
    sleep(0.8)
    print("Do you pick up the sword or leave it?")
    choice1.configure(text="Pick up",command=sword_true)
    choice2.configure(text="Leave it",command=monster)

def sword_true():
    global sword
    sword = True
    monster()  
    
def monster():
    os.system('cls')
    print("You're walking down a path until you come across a monster")
    sleep(0.8)
    global sword
    if sword == False:
        print("You have no other weapon but your hands to defend yourself")
        sleep(0.8)
        print("Something was off about the monster.")
        sleep(0.8)
        print("It seems harmless, but you don't know what other monsters might be after this one.")
        sleep(0.8)
        print("You have no other choice but to spare it.")
        choice1.configure(text="Spare", fg="blue",command=life)
        choice2.configure(text="Spare", fg="blue",command=life)

    elif sword == True:
        print("You have the sword to defend yourself!")
        sleep(0.8)
        print("But, something was off about the monster.")
        sleep(0.8)
        print("It seems harmless,but you don't know what other monsters might be after this one.")
        sleep(0.8)
        print("Do you kill or spare the monster?")
        choice1.configure(text="Kill", fg="red",command=death)
        choice2.configure(text="Spare", fg="blue",command=life)

def death():
    global monster_killed
    monster_killed = True
    os.system('cls')
    print("You raise your sword and stab the monster.")

def life():
    print("You spare the monster and it walks away from you.")
    sleep(0.8)

        





def campsite():
    os.system('cls')
    print("You chose to set up a campsite with a small tent.")
    sleep(0.8)
    print("Since it's pretty late, you fall asleep")
    sleep(0.8)
    print(".")
    sleep(0.8)
    print(".")
    sleep(0.8)
    print(".")
    sleep(0.8)
    print("Morning comes and you set out to find a way out of the forest.")
    sleep(0.8)
    print("You start walking and you come to a fork in the road.")
    sleep(0.8)
    choosing_paths()

def choosing_paths():
    print("Do you take the left or right path?")
    choice1.configure(text="Left",command=village)
    choice2.configure(text="Right",command=wrong_way)

def wrong_way():
    print("Whoops! It looks like you hit a dead end.")
    sleep(0.3)
    print("Try again!")
    choosing_paths()

def village():
    os.system('cls')
    print("Left or right?")
    sleep(0.8)



    

root = tk.Tk()
root.title("Let's Go On An Adventure!")
frame = tk.Frame(root)
frame.pack()

bottomframe = tk.Frame(root)
bottomframe.pack()

stop = tk.Button(bottomframe,text="Quit",fg="red",command=quit)
stop.pack(side=tk.BOTTOM)

start = tk.Button(frame,text="Start",command=story_start)
start.pack(side=tk.LEFT)

choice1 = tk.Button(frame,text="Cave",command=cave)
choice1.pack(side=tk.LEFT)

choice2 = tk.Button(frame,text="Campsite",command=campsite)
choice2.pack(side=tk.LEFT)




root.mainloop()