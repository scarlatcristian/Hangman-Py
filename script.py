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
display_word = " ".join(secret_word)
lives = 5

print(display_word)

while "_" in secret_word and lives > 0:
    letter = input("Guess a letter: ").lower()

    if len(letter) != 1 or not letter.isalpha():
        print("Please enter a single letter.")
        continue

    if letter in secret_word and letter in random_word:
        print("You already guessed that letter")
        print(display_word)
    elif letter in random_word:
        for position in range(len(random_word)):
            char = random_word[position]
            if char == letter:
                secret_word[position] = letter
        display_word = " ".join(secret_word)
        print(display_word)
    else:
        lives -= 1
        print(f"You guessed wrong, you have {lives} left!")
        print(display_word)


if lives <= 0:
    print(f"Game Over\nThe secret word was: {random_word}")

if "".join(secret_word) == random_word:
    print("Congratulation, you won the game")
