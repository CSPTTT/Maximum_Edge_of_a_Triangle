import random
#Allows us to use the random action to choose 'random'
import math
#Allows us to use math fn that we have to import into py
red = "\u001b[31m"

green = "\u001b[32m"

cyan = "\u001b[36m"

yellow = "\u001b[33m"

orange = "\u001b[38m"

reset_color = "\u001b[0m"

name = input("Hi, what is your name? ")
#Asks the user what their name is
print("\nHi,",name +". Let's begin!")
#Greets host and starts fn
min_value = 1000

max_value = 100

while True:

    upper_input = input("\nEnter a number > " + str(min_value) + ": ")

    try:
        number_1 = int(upper_input)
        if number_1 > min_value:
            break

        else:
            print(yellow + "Input must be greater than", str(min_value) + reset_color)
    
    except ValueError:
        print(red + "Invalid input. Please enter a valid number." + reset_color)

print(green + "\nValid input:", str(number_1) + reset_color)

while True:
    lower_input = input("\nEnter a number <" + str(max_value) + ": ")

    try:
        number_2 = int(lower_input)
        if number_2 < max_value:
            break

        else:
            print(yellow + "Input must be less than", str(max_value) + reset_color)

    except ValueError:
        print(red + "Invalid input. Please enter a valid number." + reset_color)
    
print(green + "\nValid input:", str(number_2) + reset_color
      )

upperbound = int(number_1)
#Turns upper input into an integer
lowerbound = int(number_2)
#Turns lower input into an integer
minimum_number_of_guessing = 1 + math.log2(upperbound - lowerbound + 1)
#Calculates the minimum amount of guesses it takes to get the right answer based on bounds given and stores in variable
rounded_up = math.ceil(minimum_number_of_guessing)
#Rounds up the calculation to a whole number
rounded_up_number = str (rounded_up)

selection = print(cyan + "\nI have selected a magic number between", red + str(number_2) + cyan, "and", red + str(number_1) + cyan+"." + reset_color)

magic_number = random.randint(number_2, number_1)

max_attempts = int(rounded_up_number)

attempts = max_attempts

while attempts > 0 :
    
    print("\nYou have", red + str(attempts) + reset_color, "attempts left.")

    guess_str = input("\nStart guessing! ")
    
    try:

        guess_check = float(guess_str)
    
    except ValueError:

        print ("Please enter a valid number.")

        continue    

    if guess_check < magic_number:
        
        print(yellow+"\nOops. Looks like your guess was less than the magic number. Try again. ")
    
    elif guess_check > magic_number:
        
        print(orange+"\nOops. Looks like your guess was more than the magic number. Try again. ")

    else:

        print(green + "\nHooray! You guess the magic number: ",str(magic_number) + reset_color)

        break
    
    attempts -= 1

if attempts == 0:

    print(red + "\nYou have ran out of attempts. Try again next time!\n" + reset_color)



