


print('''
*******************************************************************************
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
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

print("Welcome to Tresure Island.")
print("Your mission is to find is to find the treasure.")

choice1 = input('you\'re at a crossraod , where do you want to go? Type "left" or "right"' ).lower()

if choice1 == "left":
    choice2 = input('you\'ve come to a lake. there is an island in the middle of the lake.'
                    'type "wait" to wait for a boat.'
                    'type "swim" to swim accross').lower()
    if choice2 == "wait":
        choice3 = input('your arrived at the island unharmed .'
                         'there is house with 3 doors with .' 
                         'one red, one yellow and one blue which colur do you choose ?').lower()
        if choice3 == "red":
            print("its room full Game over")
        elif choice3 == "yellow":
            print("your found the tresure you win!")
        elif choice3 == "blue":
            print("your enter the room of beasts. Game over !")
            
    else:
        print("you got attached by an angry trout. Game Over.")





else : 
    print("your are fell in the hole , Game over!")





