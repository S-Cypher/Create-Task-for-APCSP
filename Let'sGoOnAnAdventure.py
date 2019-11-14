#Programmed by K. Stewart/S-Cypher
import tkinter as tk
from time import sleep
import os
os.system('cls')
print("Press 'Start' to start the adventure!")

sword = False
monster_killed = False
left_taken = False


def story_start():
    os.system('cls')
    start.pack_forget()
    print("You're exploring a forest when you come across a cave.")
    sleep(0.8)
    print("You've been traveling for a long time and you're tired but, the cave intrigues you.")
    sleep(0.8)
    print("Do you travel in the cave or make a campsite?")
    choice1.pack(side = tk.LEFT)
    choice2.pack(side = tk.LEFT)

    
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
        choice1.configure(text="Spare",command=life)
        choice2.configure(text="Spare",command=life)

    elif sword == True:
        print("You have the sword to defend yourself!")
        sleep(0.8)
        print("But, something was off about the monster.")
        sleep(0.8)
        print("It seems harmless,but you don't know what other monsters might be after this one.")
        sleep(0.8)
        print("Do you kill or spare the monster?")
        choice1.configure(text="Kill",command=death)
        choice2.configure(text="Spare",command=life)

def death():
    global monster_killed
    monster_killed = True
    os.system('cls')
    print("You raise your sword and stab the monster.")
    sleep(0.8)
    print("You continue on in the cave.")
    sleep(2.2)
    maze()

def life():
    os.system('cls')
    print("You spare the monster and it walks away from you.")
    sleep(0.8)
    print("You continue on in the cave.")
    sleep(2.2)
    maze()

def maze():
    os.system('cls')
    print("You are determined to find a way out of the cave.")
    sleep(0.8)
    print("After walking a couple of steps, you find three paths.")
    sleep(0.8)
    print("Which way do you go?")
    choice1.configure(text= "Left", command = left_path)
    choice2.configure(text = "Forward", command = forward_path)
    choice3.pack(side = tk.LEFT)
def show_code():
    print("The numbers were: 88431")
    sleep(2.4)
    maze()

def left_path():
    os.system('cls')
    global left_taken
    if left_taken == True:
        print("You've already gone this way. There's nothing else to see.")
        sleep(0.8)
        print("Do you need to see the numbers again?")
        choice3.pack_forget()
        choice1.configure(text = "Yes", command = show_code)
        choice2.configure(text = "No", command = maze)
    else:
        print("The left path goes straight into a dead end.")
        sleep(0.8)
        print("But there is a note on the wall.")
        sleep(0.8)
        print("It has the numbers: 88431")
        sleep(0.8)
        print("Since you don't know what those numbers mean, you head back to the three paths.")
        sleep(3.0)
        left_taken = True
        maze()
  
def forward_path():
    os.system('cls')
    print("You move forward")
    
def right_path():
    os.system('cls')
    print("You turn right")
#############################    
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
    choice2.configure(text="Right",command=small_hut)

def small_hut():
    os.system('cls')
    print("You took the right path and came upon a small hut.")
    

def village():
    os.system('cls')
    print("You took the left path and found a small hut")
    

root = tk.Tk()
root.title("Let's Go On An Adventure!")
frame = tk.Frame(root)
frame.pack()

bottomframe = tk.Frame(root)
bottomframe.pack()
####
stop = tk.Button(bottomframe,text="Quit",fg="red",command=quit)
stop.pack(side=tk.BOTTOM)

start = tk.Button(frame,text="Start", activebackground = "aliceblue",command=story_start)
start.pack(side=tk.LEFT)

choice1 = tk.Button(frame,text="Cave",command=cave)
choice2 = tk.Button(frame,text="Campsite",command=campsite)
choice3 = tk.Button(frame, text= "Right", command = right_path)

root.mainloop()
