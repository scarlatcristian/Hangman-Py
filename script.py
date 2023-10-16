import random

print("""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
      """)

words_list = ["beekeeper", "skeleton", "robot",
              "mouse", "orange", "arrived", "upscale"]

random_word = random.choice(words_list)
secret_word = ["_"] * len(random_word)
lives = 5

print(" ".join(secret_word))
x = 0

while "_" in secret_word and lives > 0:
    letter = input("Guess a letter: ").lower()

    if len(letter) != 1 or not letter.isalpha():
        print("Please enter a single letter.")
        continue

    if letter in secret_word and letter in random_word:
        print("You already guessed that letter")
        print(" ".join(secret_word))

    elif letter in random_word:
        for index, char in enumerate(random_word):
            if char == letter:
                secret_word[index] = letter
        print(" ".join(secret_word))
    else:
        lives -= 1
        print(f"You guessed wrong, you have {lives} left!")
        print(" ".join(secret_word))


if lives <= 0:
    print(f"Game Over\nThe secret word was: {random_word}")

if "".join(secret_word) == random_word:
    print("Congratulation, you won the game")
