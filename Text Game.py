#Keira Stewart
#Let'sGoInACave!.py is the original file that I haven't touched in almost 4 years
#Text Game.py (this file) is a copy of the original with my recent comments about it.
'''
Short background about this project:
I made this code in 10th grade with a small understanding of the tkinter library.
I was learning about the window, functions, and buttons in tkinter as I was making this project
This was for AP Computer Science Principles although I didn't take the test nor does SLU even accept the credit for that test.
I've placed updated comments to try to understand my thoughts from 10th grade and for anyone else who might see the code

'''
#1900 by 1020 px (I still do not know why this is here. Maybe this was my laptop's screen size? Or the tkinter's window size?)
import tkinter as tk
from time import sleep #I only used sleep to make reasonable pauses between text lines. It felt so weird for all of the function's text to print at once
import os
import asciiart #Might not use ascii art if I want to remake this. 
#It's possible, but I don't feel like dealing with it again. 
os.system('cls')  #clears the terminal; it works on most terminals, I have yet to see where it doesn't work
print("Press start to begin!")

times_died = 0
sword = False
monster_killed = False
shield = False
inventory = ['torch'] #hahaha using an inventory system was interesting.
#I just remember understanding how to add and remove items in a regular list with things like .append, and .pop ,I think?

#These variables have to be global otherwise the program can't check for certain choices -10th grade me
#This was when I was learning about global vs local variables! :) - College freshman me
def reset_variables():
  global sword
  global monster_killed
  global shield
  sword = False
  monster_killed = False
  shield = False
  welcome_back()


def welcome_back(): #This is to count how many times the player has died.
  #But it only activates when they've played and died at least once.
  os.system('cls')
  print("Welcome back!")
  sleep(0.8)
  print("You have died", times_died, "times.")
  sleep(0.8)
  print("Let's try again!")
  sleep(2.5)
  story_start()
  '''
    I think all of the function names are pretty easy to understand what's inside of them.
    That was more for me to understand where there could be a problem
    If something wasn't printing or something, I could find the error in this function
    '''

def story_start():
  os.system('cls')
  start.pack_forget() #I think this was to clear the buttons in the tk window
  print("You're exploring a forest when you come across a cave.")
  sleep(0.8)
  print("You decide to explore the cave.")
  sleep(1.8)
  cave()
    
def cave():
  os.system('cls')
  print("The cave is dark but you found a torch on the way in.")
  sleep(0.8)
  print("You come across a sword on the ground")
  sleep(0.8)
  asciiart.sword() #prints the sword from the asciiart file
  sleep(0.8)
  print("Do you pick up the sword or leave it?")
  choice1.configure(text = "Leave it",command=monster)
  choice2.configure(text = "Pick up", command =sword_true)

def sword_true(): #I don't like this function, but I couldn't think of another way to know if the player picked up the sword
  global sword
  sword = True
  inventory.append("Sword")
  monster()
  
#I HAVE to come up with a better story. Jesus, I did not like trying to come up with this at the start. It felt awkward.    
def monster():
  os.system('cls')
  print("You're walking down a path until you come across a monster")
  sleep(0.8)
  asciiart.monster
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

  elif sword == True: #Why did I do an elif here? It's Boolean! There's only two choices!!
      print("You have the sword to defend yourself!")
      sleep(0.8)
      print("But, something was off about the monster.")
      sleep(0.8)
      print("It seems harmless,but you don't know what other monsters might be after this one.")
      sleep(0.8)
      print("Do you kill or spare the monster?")
      choice1.configure(text="Kill",command=death)
      choice2.configure(text="Spare",command=life)

def death(): #Should rename this...
  global monster_killed
  monster_killed = True
  os.system('cls')
  print("You raise your sword and stab the monster.")
  sleep(0.8) #By the looks of these MULTIPLE sleep lines, I should just let all of the text print as once. 
  print("Near the monster's body, there's a piece of paper.")
  sleep(0.8)
  print("It reads: 88431") #I'm probably not going to make the player enter any kind of code. I could, but it seems a bit excessive for right now
  sleep(0.8)
  print("You're confused by the paper")
  sleep(0.8)
  print("But, you continue on in the cave.")
  inventory.append("code paper")
  sleep(2.2)
  maze()

def life():
  os.system('cls')
  print("You spare the monster and it gives you a piece of paper.")
  sleep(0.8)
  print("The paper reads: 88431")
  sleep(0.8)
  print("You don't know what those numbers mean.")
  sleep(0.8)
  print("But, you continue on in the cave.")
  inventory.append("code paper") #I miss using lists for python projects.
  sleep(2.2)
  maze()

def maze():
  os.system('cls')
  print("You are determined to find a way out of the cave.") #I hated this line when I first did this! It feels weird.
  sleep(0.8)
  print("After walking a couple of steps, you find two paths.")
  sleep(0.8)
  print("Which way do you go?")
  choice1.pack_forget()
  choice2.configure(text = "Straight", command = forward_path)
  choice3.pack(side = tk.LEFT)
  
def forward_path():
  os.system('cls')
  print("You decide to go down the straight path.")
  sleep(0.8)
  print("You seem to have attracted a bear...")
  asciiart.bear()
  sleep(0.8)
  print("Unlike the first monster, this bear seems hostile.")
  sleep(0.8)
  battle_choice()
 
def bear_battle():
  os.system('cls')
  print("Alright! Time for some action!")
  sleep(1.6)
  print("You look into your inventory to find some items.")
  

  if sword == True:
    os.system('cls')
    print("You have your sword.")
    sleep(0.8)
    print("But it doesn't seem like the sword alone will help you fight the bear.")
    sleep(0.8)
    print("Do you also want to use your torch?")
    choice1.configure(text="Torch",command = yes_torch)
    choice2.configure(text="No torch", command = bear_battle)
    choice3.pack_forget()

  else:
    os.system('cls')
    print("It seems that you don't have anything to fight against the bear...")
    sleep(2.8)
    print("You try to attack with your fists but the bear has a huge advantage.")
    sleep(1)
    print("The bear roars and slashes you across the chest.")
    sleep(0.8)
    print("You have died from blood loss.")
    sleep(1.6)
    death_message()
 
def escape():
  os.system('cls')
  print("Scared by the bear, you ran back to the three paths.")
  sleep(2)
  maze()

def battle_choice():
  os.system('cls')
  print("Do you want to battle the bear?")
  choice1.configure(text="Yes", command= bear_battle)
  choice2.configure(text="No", command = escape)
  choice3.pack_forget()

def yes_torch():
  global fight_w_torch
  fight_w_torch = True
  bear_battle()

def right_path():
  os.system('cls')
  print("You turn right")
  sleep(0.8)
  print("Nothing here...")
  sleep(1.8)
  print("Two more paths are ahead: Left and Straight")
  sleep(0.8)
  print("Where are you going next?")
  choice1.configure(text="Left", command=next_left)
  choice2.configure(text="Straight", command=shield_straight)
  choice3.pack_forget() #Oh yeah, pack_forget() DOES remove the button from the pack


def next_left():
  os.system('cls')
  print("Nothing to see here.")
  sleep(0.8)
  print("Three more paths are around you: Left, Straight, and Right")
  sleep(0.8)
  print("Where are you going next?")
  sleep(0.8)
  choice1.configure(text="Left", command = left_treasure)
  choice2.configure(text = "Straight", command = normal_straight) #I didn;t make normal_straight() and dead_end() yet...
  choice3.configure(text = "Right", command = dead_end) #I don't remember when I stopped working on this game
  choice3.pack(side=tk.LEFT)


def left_treasure():
  os.system('cls')
  print("Hello. Test text!") #hahahaha


  
def shield_straight():
  os.system('cls')
  global times_died
  print("Going straight, you find a shield.")
  sleep(0.8)
  asciiart.shield()
  global sword
  if sword == False:
    if times_died > 0:
      print("Honestly, you might want to pick up the shield...")
      sleep(0.8)
      print("You died", times_died, "times. It'll help you with other things in the cave.")
    elif times_died == 0:
      print("Since you haven't died yet, this could prevent that from happening.")
  elif sword == True:
    print("This can add more protection")
  sleep(0.8)
  choice1.configure(text="Shield", command = a_shield)
  choice2.configure(text="No shield", command = no_shield)
  choice3.pack_forget()


def a_shield():
  os.system('cls')
  print("You pick up the shield.")
  sleep(0.8)
  inventory.append('Shield')
  print("It has been added to your inventory.")

def no_shield():
  os.system('cls')
  print("Alright, that's your funeral...")
  sleep(0.8)
  

def death_message():
  global times_died
  times_died += 1 #When the player starts the game again, it tells them how many times they have died.
  os.system('cls')
  print("It seems you have died...")
  sleep(0.8)
  print("Do you want to restart or quit the game?")
  choice1.configure(text="Restart",command=reset_variables)
  choice2.configure(text="Quit", command= quit)
  choice3.pack_forget()

#Non-story stuff. The code to create the window, buttons, and other things
root = tk.Tk()
root.title("Cave Adventure!") #Titles the screen
frame = tk.Frame(root)
frame.pack()

bottomframe = tk.Frame(root)
bottomframe.pack()

start = tk.Button(frame,text="Start", activebackground="aliceblue",command=story_start)
start.pack(side=tk.LEFT)

choice1 = tk.Button(frame)
choice1.pack(side=tk.LEFT)

choice2 = tk.Button(frame)
choice2.pack(side=tk.LEFT)

choice3 = tk.Button(frame, text= "Right", command = right_path)
#I mainly have two choices for every decision, this button command is just here for the one time I needed three choices

root.mainloop() #mainloop does something, I just forgot. I think it keeps the window open and working?
