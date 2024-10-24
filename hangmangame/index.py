import random

def hangman():
    # List of words the game can randomly select from.
    words = ['python', 'hangman', 'programming', 'challenge', 'openai', 'assistant']
    secret_word = random.choice(words)  # Pick a word at random.
    letters_to_guess = set(secret_word)  # Unique letters in the chosen word.
    guessed_letters = set()  # Letters the player has already guessed.
    attempts = 6  # Maximum incorrect guesses allowed.

    print("\nLet's play Hangman!")
    print("Try to guess the word, letter by letter.")

    # Keep looping until the player runs out of attempts or guesses the word.
    while len(letters_to_guess) > 0 and attempts > 0:
        # Create the word display, showing guessed letters and hiding others.
        current_display = [ch if ch in guessed_letters else '_' for ch in secret_word]
        print('Current word: ', ' '.join(current_display))
        print(f"Remaining attempts: {attempts}")
        print(f"Guessed letters so far: {', '.join(sorted(guessed_letters)) or 'None'}")

        # Ask the player for a letter and ensure it's valid.
        guess = input("\nGuess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter from A to Z.")
            continue

        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try something else.")
            continue

        # Add the guessed letter to the set.
        guessed_letters.add(guess)

        if guess in letters_to_guess:
            letters_to_guess.remove(guess)  # Remove correctly guessed letter from the set.
            print(f"Nice! '{guess}' is in the word.")
        else:
            attempts -= 1  # Reduce attempts for an incorrect guess.
            print(f"Oops! '{guess}' is not in the word.")

        print("-" * 40)

    # Final game messages after the loop ends.
    if attempts == 0:
        print(f"Out of attempts! The word was '{secret_word}'. Better luck next time!")
    else:
        print(f"Congratulations! You've guessed the word '{secret_word}'.")

# Entry point of the program.
if __name__ == "__main__":
    hangman()
