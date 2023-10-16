import random
#Allows us to use the random fn

cyan = "\u001b[36m"
reset_color = "\u001b[0m"
green = "\u001b[32m"
red = "\u001b[31m"
orange = "\u001b[38m"

host_name = input("\nPlease input your name: ")

print ("\nHi,", cyan + host_name + reset_color + ". Let's play the guessing word game!")

magic_word_bank_1 = ["maroon", "navy", "olive", "teal", "indigo", "coral", "mauve", "charcoal", "ivory", "slate"]

#horscope
#gems
#food
#states

#magic_word_banks = [magic_word_bank_1, magic_word_bank_2, magic_word_bank_3, magic_word_bank_4]

#magic_word_bank = random.choice(magic_word_banks)

magic_word = random.choice(magic_word_bank_1)

selected_magic_word = ["_" for _ in magic_word]

max_attempt = 10
attempts = 0

def if_letter_in_magic_word(letter, selected_magic_word):
    return letter in magic_word

game_over = False

while not game_over:
     print("\n" + " ".join(selected_magic_word))

     host_guess = input("\nGuess a letter: ").lower()

     if len(host_guess) != 1 or not host_guess.isalpha():
          print("\n",red+"Please enter a single letter" + reset_color)
          continue
     
     letter_found = False
     
     for i in range(len(magic_word)):
         if magic_word[i] == host_guess:
            selected_magic_word[i] = host_guess
            letter_found = True
        
     if not letter_found:
        attempts += 1
        print(red + "\nIncorrect guess. Attempts remaining: ", str(max_attempt - attempts) + reset_color + "\n")
            
     if "_" not in selected_magic_word:
         print(green + "\nCongratulations!" + reset_color,"You guessed the word correctly:", green + "".join(selected_magic_word).replace(" ","") + reset_color + "\n")
         game_over = True
         break
             
if "_" in selected_magic_word:
    print(red + "Out of attempts. The word was:", magic_word.replace(" ", "") + reset_color)
 
#TASK
#Doesn't send out the Out of attempts when attempts remaining == 0; need to include into the game loop as a break
#Needs to tell the user what the words was if the word is not guessed in time


