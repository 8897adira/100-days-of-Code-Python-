import random


word_list = ["sunset", "horizon", "breeze", "tranquility", "mountain", "forest", "adventure", "ocean", "twilight", "dream", "courage", "wisdom", "strength", "discovery", "journey", "serenity", "freedom", "passion", "harmony", "bliss"]


word = random.choice(word_list)
blanks = ["_"] * len(word)  # Create a list of blanks
attempts = 6  # Number of incorrect guesses allowed
guessed_letters = []  # Store guessed letters


def display_blanks():
    print(" ".join(blanks))


def display_hangman(attempts_left):
    stages = [
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / 
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |   
           |
        """,
        """
           ------
           |    |
           |    O
           |    
           |   
           |
        """,
        """
           ------
           |    |
           |    
           |    
           |   
           |
        """,
        """
           ------
           |    
           |    
           |    
           |   
           |
        """,
        """
           ------
           |    
           |    
           |    
           |   
           |
        """
    ]
    print(stages[attempts_left]) 
# Game Loop
print("Welcome to Hangman!")

while attempts > 0:
    print("\nAttempts remaining:", attempts)
    display_hangman(attempts)  # Display the hangman
    display_blanks()  # Display the blanks
    
    # Get user input
    guess = input("Guess a letter: ").lower()

    # Check if the letter has already been guessed
    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try a different letter.")
        continue

    guessed_letters.append(guess)  # Add the guessed letter to the list

    # Check if the guessed letter is in the word
    if guess in word:
        print(f"Good guess! '{guess}' is in the word.")
        # Update the blanks with the correct letter
        for i in range(len(word)):
            if word[i] == guess:
                blanks[i] = guess
    else:
        print(f"Sorry, '{guess}' is not in the word.")
        attempts -= 1  # Decrease attempts for incorrect guess

    # Check if the player has guessed the whole word
    if "_" not in blanks:
        print("\nCongratulations! You've guessed the word:", word)
        break

# Check if the player ran out of attempts
if attempts == 0:
    display_hangman(attempts)  # Show final hangman
    print("\nGame over! You've run out of attempts.")
    print("The word was:", word)
