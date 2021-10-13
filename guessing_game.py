import random

target_guess = random.randint(0, 10)

while 1:
    user_input = input("Please enter your chosen number:")
    user_input = int(user_input)
    if user_input == target_guess:
        print("You have guessed correctly. Well done! \n")

        break
    else:
        print("Please guess again. \n")
