import random
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
letter_total = input("how many letters would you like in your password?\n")
symbols_total = input("how many symbols would you like in your password?\n")
numbers_total = input("how many numbers would you like in your password?\n")

total_char = int(letter_total)+int(symbols_total)+int(numbers_total)
total_letters = 0
total_numbers = 0
total_symbols = 0
password = []
restart = True
while restart:
  for x in range(total_char):
    char_option = random.randint(0,2)
    if char_option ==0 and total_letters != int(letter_total):
      password.append(random.choice(letters))
      total_letters+=1
    elif char_option==1 and total_numbers != int(numbers_total):
      password.append(random.choice(numbers))
      total_numbers+=1
    elif char_option ==2 and total_symbols != int(symbols_total):
      password.append(random.choice(symbols))
      total_symbols+=1
    if len(password) == total_char:
      restart = False
new_password=''
print (f"Your new password is: {new_password.join(password)}")

# print(f"char len = {total_char}")
#
# print(f"num total = {total_numbers}")
#
# print(f"sym total = {total_symbols}")
#
# print(f"let total = {total_letters}")
