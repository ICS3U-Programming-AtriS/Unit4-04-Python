#!/usr/bin/env python3
# Created By: Atri Sarker
# Date: April 23, 2025
# Random number guessing program
# that keeps on looping until the user guesses the number

import random


def main():
    # Generate the correct number,
    # a random number between 0 and 9
    correct_num = random.randint(0, 9)

    # LOOP
    while True:
        # Get the user's guess as a string
        user_input = input("Guess a number (0-9): ")

        try:
            # Convert the user's guess to an integer
            user_num = int(user_input)

            # Check if the user's guess is the same as the correct number
            if user_num == correct_num:
                # Tell the user that they guessed correctly
                print("You guessed correctly!")
                # Break the Loop
                break
            # If it isn't, tell the user that they guessed wrong
            else:
                # Tell the user that they guessed wrong
                print(f"Wrong! Try again.")
        except ValueError:
            # Tell the user that their input wasn't an integer
            print(f"{user_input} is not an integer. Please try again!")

    # Program completion message
    print("Thanks for Playing!")


if __name__ == "__main__":
    main()
