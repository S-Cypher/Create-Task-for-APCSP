#K.Stewart
#AP Computer Science Principles

import tkinter as tk
from time import sleep
import os

os.system('cls')
print("Press 'Start' to start the adventure!")

sword = False

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
        print("You punch the monster, but it had no affect")
        sleep(0.8)
    elif sword == True:
        print("You have the sword to defend yourself!")




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
