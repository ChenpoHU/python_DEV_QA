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

feedOrNot = input(seeMonster + "The see monster is following you. You have a fish, do you want to feed it with the fish? \n Type Yes/No: ").lower()
if feedOrNot == "yes":
    print("Thank you for feeding me! I have a four luck chararcters for you: NOPE. You will be able to open the treasure box by rearranging these four characters.")
elif feedOrNot == "no":
    print("You can eat the fish yourself, so than you will not endure the hunger.")


openOrNot = input(treasureRoom + "\n You arrived the cave with the treasure box on the island! Please enter the password of four characters \n " + treasureLock).lower()
if openOrNot == "open":
    print("You WIN!")
else:
    print("Game Over.")




