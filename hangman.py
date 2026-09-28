import random

# List of words
words = ["divya", "computer", "python", "college", "coding"]

# Choose a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of wrong guesses allowed
wrong_guesses = 0
max_wrong_guesses = 6

print("===== HANGMAN GAME =====")
print("Guess the word one letter at a time.")
print("You have 6 wrong guesses.")

# Game loop
while wrong_guesses < max_wrong_guesses:

    # Display the word
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if the word is completely guessed
    if all(letter in guessed_letters for letter in word):
        print("Congratulations! You guessed the word.")
        print("The word was:", word)
        break

    # Take user input
    guess = input("Enter a letter: ").lower()

    # Check whether input is a single letter
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add letter to guessed list
    guessed_letters.append(guess)

    # Check the guess
    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")
        print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)

else:
    print("\nGame Over!")
    print("The correct word was:", word)