import time
import random

words = ["Horizon", "Velvet", "Lantern", "Whistle", "Meadow", "Quiver", "Twilight", "Ponder", "Brisk", "Echo",
         "Glimmer", "Mirth", "Sizzle", "Wander", "Plume", "Jolly", "Fable", "Dusk", "Zookeeper", "Lush"]

word = random.choice(words)
guessed_word = ['_'] * len(word)
attempts = 6
guessed_letters = []

print('Hello, welcome to Hangman! :D')
time.sleep(1)
print('Guess the word: ')

while attempts > 0:
    print(" ".join(guessed_word))
    print(f"You have {attempts} attempts remaining.")
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a valid single letter!")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter, try again!")
        continue

    guessed_letters.append(guess)

    if guess in word.lower():
        print(f"Good guess! {guess} is in the word.")

        for index in range(len(word)):
            if word[index].lower() == guess:
                guessed_word[index] = word[index]
    else:
        attempts -= 1
        print(f"Oops! {guess} is not in the word.")


    if "_" not in guessed_word:
        print(f"Congratulations! You've guessed the word: {word} :D")
        break
else:
    print(f"Game Over! The word was: {word}. Good try!")



