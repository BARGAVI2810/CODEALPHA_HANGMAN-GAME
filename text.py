import random

# List of 5 predefined words
word_list = ['python', 'hangman', 'program', 'computer', 'code']

# Randomly choose a word from the list
secret_word = random.choice(word_list)

# Initialize variables
guessed_letters = []
attempts_left = 6

# Create a display with underscores for each letter in the word
display_word = ['_'] * len(secret_word)

print("🎮 Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have 6 incorrect guesses. Let's go!\n")

# Game loop
while attempts_left > 0 and '_' in display_word:
    print("Word: " + ' '.join(display_word))
    print(f"Guessed letters: {', '.join(guessed_letters)}")
    print(f"Attempts left: {attempts_left}")
    
    guess = input("Enter a letter: ").lower()

    # Validate single letter input
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter a single alphabet letter.\n")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("❗ You've already guessed that letter. Try a different one.\n")
        continue

    # Add the guess to guessed letters
    guessed_letters.append(guess)

    # Check if the guess is in the word
    if guess in secret_word:
        print("✅ Good guess!\n")
        # Update the display word
        for index in range(len(secret_word)):
            if secret_word[index] == guess:
                display_word[index] = guess
    else:
        print("❌ Wrong guess!\n")
        attempts_left -= 1

# Check win or lose
if '_' not in display_word:
    print("🎉 Congratulations! You guessed the word: " + secret_word)
else:
    print("💀 Game Over! The word was: " + secret_word)
