
import random as rd
words_list = ["laptop" , "jumping" , "Free Fire"]

 
choosed_word = rd.choice(words_list)
print(choosed_word)

#------------------------------------------------
placeholder = ""
words_lenght = len(choosed_word)
for position in range (words_lenght):
    placeholder += "_"
print(placeholder)

#---------------------------------------------------------- 
game_over = False
correct_list = []
while not game_over:
    guess = input("Guess the letter:")

#----------------------------------------------------------

    display = ""
    for letter in choosed_word:
        if letter == guess:
            display += letter 
            correct_list.append(letter)

        elif letter in correct_list:
            display += letter
        else:
            display += '_'  
    print(display)

    #------------------------------------------------------------

    if '_' not in display:
        game_over = True
        print("You Win!")
    







