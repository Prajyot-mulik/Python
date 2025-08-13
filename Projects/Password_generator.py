import random
letter = ['a', 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't','u' , 'v' , 'w', 'x' , 'y' ,'z']
number = ['1', '2', '3' , '4' , '5' , '6' , '7' , '8' , '9']
symbols = ['!' , '#' , '$' , '%' , '&' , '*']


print("Welcome to the pyPassword generator!")

np_letters = int(input("How many letters whould you like in your password \n?"))
np_symbols = int(input("how many symbols would you like \n ?"))
np_number = int(input("how many numbers in your password ?"))
      

# pass_list = []

# pass_list += random.choices(letter , k=np_letters)
# pass_list += random.choices(letter , k=np_number)
# pass_list += random.choices(letter , k=np_symbols)


# password = ''.join(pass_list)

# print(password)

password = []

for char in range(0 , np_letters):
    password.append (random.choice(letter))
    

for char in range(0 , np_number):
    password.append (random.choice(number))
    
for char in range(0 , np_symbols):
    password.append (random.choice(symbols))

print(password)        
random.shuffle(password)
print(password)
    
passwords = ""
for char in password:
    passwords += char 

print(f"your password is: {passwords}")
