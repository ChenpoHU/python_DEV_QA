import random
import time

welcome = '''
                  _____$$$$___________$$$$
               __$$$$$$$$$_______$$$$$$$$$__
              __$$$$$$$$$$$_____$$$$$$$$$$$__
             __$$$$$$$$$$$$$___$$$$$$$$$$$$$__        
            __$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
            __$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
             __$$$$$$$$$$$$$$$$$$$$$$$$$$$$__
              __$$$$$$$$$$$$$$$$$$$$$$$$$$__
                __$$$$$$$$$$$$$$$$$$$$$$__
                  __$$$$$$$$$$$$$$$$$$__
                     __$$$$$$$$$$$$__
                          $$$$
                          $$$$
                          $$$$
                          $$$$
                          $$$$
                          $$$$     WELCOME
                          $$$$       TO
                          $$$$     TREASURE
                          $$$$       BOX
                          $$$$  PLEASE CONFIGURE YOUR TREASURE BOX FIRST!
'''

seeMonster = '''
           /\_/!
          / o o !
         /   ^   !
       ( ======== )
        )"""""""(
       /         !
      (           )
     ( (  )   (  ) )
    (__(__)___(__)__)

              ~ ~ ~ ~~~
'''

boat = '''
            /\            
           /  \           
          /    \          
         /      \         
        /        \        
   ____/__________\____   
  |                    ,_˜
  |                     > ˜˜˜˜˜
  |                ____`-' ˜˜˜˜˜˜˜
   \                 )`-_> ˜˜˜˜˜˜˜˜˜˜
    \_______________)     )-`-` 
'''

treasureRoom = '''
  /¯¯¯¯¯¯¯¯¯¯¯¯
 |  ▓▓▓▓▓▓▓▓▓▓  |
 |  ▓▓▓▓▓▓▓▓▓▓  |
 |  ▓▓╔════╗▓▓  |
 |  ▓▓║    ║▓▓  |
 |  ▓▓║    ║▓▓  |
 |  ▓▓╚════╝▓▓  |
 |  ▓▓▓▓▓▓▓▓▓▓  |
 |  ▓▓▓▓▓▓▓▓▓▓  |
  \____________/
  '''

treasureBox = '''
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| TREASURE  `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._ BOX      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
___/______/______/______/______/______/______/______/______/______/_____ /__ /
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

'''

treasureLock = '''
 _________________________________________
/                                         
|  1  |  2  |  3  |  4  |  5  |  6  |  7  |
|-----------------------------------------|
|  8  |  9  |  0  |  A  |  B  |  C  |  D  |
|-----------------------------------------|
|  E  |  F  |  G  |  H  |  I  |  J  |  K  |
|-----------------------------------------|
|  L  |  M  |  N  |  O  |  P  |  Q  |  R  |
|-----------------------------------------|
|  S  |  T  |  U  |  V  |  W  |  X  |  Y  |
|-----------------------------------------|
|  Z  |  !  |  @  |  #  |  $  |  %  |  ^  |
|-----------------------------------------|
|  &  |  *  |  (  |  )  |  -  |  _  |  +  |
|-----------------------------------------|
|  =  |  {  |  }  |  [  |  ]  |  \  |  |  |
|-----------------------------------------|
|  :  |  ;  |  "  |  '  |  <  |  >  |  ?  |
\_________________________________________/
  '''

rock = '''

     _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

paper = '''

    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

'''

scissor = '''

    _______
---'   ____)____
      __________)
   _____________)
  (_______)
---.______)

'''

print(welcome)

# Prompt the user to enter the characters to use for the top and bottom of the box
top_bottom_char = input("Enter the character you want to use for the top and bottom of the treasure box: ")

# Prompt the user to enter the character to use for the sides of the box
side_char = input("Enter the character you want to use for the sides of the treasure box: ")

# Prompt the user to enter the character to use for the lock of the box
lock_char = input("Enter the character you want to use for the lock of the treasure box: ")

# Build the treasure box as a multi-line string using the entered characters
treasure_box = f'''
{top_bottom_char * 9}
{side_char}@{" " * 7}@{side_char}
{side_char}@{" " * 7}@{side_char}
{side_char}@{" " * 3}{lock_char}{" " * 3}@{side_char}
{side_char}@{" " * 7}@{side_char}
{side_char}@{" " * 7}@{side_char}
{top_bottom_char * 9}
'''

# Print the treasure box
print("This is the treasure box that you are looking for:\n " + treasure_box)

print("I found one treasure box similar to this one:\n " + treasureBox)

shipOrMonster = input("Your map shows that you need to get to Treasure Island, you can wait to board a boat or swim accross the sea, pick one.\nType Swim/Boat: ").lower()
if shipOrMonster == "swim":
    print(seeMonster + "\n Unfortunately, you were eaten by the hungry see monster, try again.")
elif shipOrMonster == "boat":
    print("Nice, you made it to the next level, you're pretty good at this!")
    print ("Welcome to the boat:\n ")
    print (boat + "\n")
    time.sleep(1)

feedOrNot = input(seeMonster + "The see monster is following you. You have a fish, do you want to feed it with the fish? \n Type Yes/No: ").lower()

choice = (input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n0/1/2:"))
seeMonster_choice = random.randint(0,2)

if feedOrNot == "yes":
    print("Thank you for feeding me! I have a four luck chararcters for you. You will be able to open the treasure box by rearranging these four characters. But you need to play the rock, paper and scissor with me and win first.")
    if not choice.isdigit():
        print("You've entered an invalid value, try again and choose a number between 0-2.")
    else:
        choice = int(choice)
    if choice > 2:
        print("You've entered an invalid number, try again and choose a number between 0-2.")
    elif choice == 0 or choice == 1 or choice == 2:
        if choice == 0:
            print(f"You chose: Rock {rock}")
        elif choice == 1:
            print(f"You chose: Paper {paper}")
        elif choice == 2:
            print(f"You chose: Scissor {scissor}")

        if seeMonster_choice == 0:
            print(f"The see Monster chose: Rock {rock}")
            if choice == 2:
                print("You lose, Rock wins against scissor.")
            elif choice == 0:
                print("It's a draw!")
            else:
                print("You win! The four lucky character is NOPE")

        elif seeMonster_choice == 1:
            print(f"The see Monster chose: Paper {paper}")
            if choice == 0:
                print("You lose, Paper wins against rock.")
            elif choice == 0:
                print("It's a draw!")
            else:
                print("You win!The four lucky character is NOPE")

        elif seeMonster_choice == 2:
            print(f"The see Monster chose: Scissors {scissor}")
            if choice == 1:
                print("You lose, Scissor win against paper.")
            elif choice == 2:
                print("It's a draw!")
            else:
                print("You win!The four lucky character is NOPE")

elif feedOrNot == "no":
    print("You can eat the fish yourself, so than you will not endure the hunger.")


openOrNot = input(treasureRoom + "\n You arrived the cave with the treasure box on the island! Please enter the password of four characters \n " + treasureLock).lower()
if openOrNot == "open":
    print("You WIN!")
else:
    print("Game Over.")




