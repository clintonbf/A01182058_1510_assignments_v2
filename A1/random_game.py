import random
import doctest


def check_guess_is_valid(player_guess):
    """
    Assign a number to player's guess.

    :param player_guess: string
    :precondition: any string
    :postcondition: assigns a different number if player's guess is "rock", "paper", "scissors", or invalid
    :return: int

    >>> check_guess_is_valid("paper")
    1
    >>> check_guess_is_valid("booger")
    4
    >>> check_guess_is_valid("    rOck")
    0
    """
    player_guess = player_guess.strip()

    if player_guess.lower() == "rock":
        return_code = 0
    elif player_guess.lower() == "paper":
        return_code = 1
    elif player_guess.lower() == "scissors":
        return_code = 2
    else:
        return_code = 4

    return return_code


def check_rock(comp_guess):
    """
    Check user's play against the computer's.

    :param comp_guess: int
    :precondition: 0 < argument < 2
    :precondition: argument is an integer
    :postcondition: the winner in a round of rock, paper, scissors
    :return: string

    >>> check_rock(2)
    'Rock beats scissors: you win!'
    """

    if comp_guess == 0:
        return "Rock and rock: tie!"
    elif comp_guess == 1:
        return "Paper beats rock: you lose!"
    elif comp_guess == 2:
        return "Rock beats scissors: you win!"


def check_paper(comp_guess):
    """
       Check user's play against the computer's.

       :param comp_guess: int
       :precondition: 0 < argument < 2
       :precondition: argument is an integer
       :postcondition: the winner in a round of rock, paper, scissors
       :return: string

       >>> check_paper(2)
       'Scissors beat paper: you lose!'
       """

    if comp_guess == 0:
        return "Paper beats rock: you win!"
    elif comp_guess == 1:
        return "Paper and paper: tie!"
    elif comp_guess == 2:
        return "Scissors beat paper: you lose!"


def check_scissors(comp_guess):
    """
       Check user's play against the computer's.

       :param comp_guess: int
       :precondition: 0 < argument < 2
       :precondition: argument is an integer
       :postcondition: the winner in a round of rock, paper, scissors
       :return: string

       >>> check_scissors(2)
       'Scissors and scissors: tie!'
       """

    if comp_guess == 0:
        return "Rock beats scissors: you lose!"
    elif comp_guess == 1:
        return "Scissors cut paper: you win!"
    elif comp_guess == 2:
        return "Scissors and scissors: tie!"


def rock_paper_scissors():
    """
    Play a round of rock, paper, scissors with user
    """

    comp_guess = random.randint(0, 2)
    your_guess = input("What's your guess, punk? ")

    num_guess = check_guess_is_valid(your_guess)

    if num_guess == 4:
        print("Invalid guess. Only 'rock', 'paper', or 'scissors' are valid.")
    else:
        if num_guess == 0:  # rock
            print(check_rock(comp_guess))
        elif num_guess == 1:  # paper
            print(check_paper(comp_guess))
        elif num_guess == 2:  # scissors
            print(check_scissors(comp_guess))


def main():
    # Test 1: rock
    # Test 2: paper
    # Test 3: scissors
    # Test 4: ROCK
    # Test 5: '   ROCK'
    # Test 6: chicken
    # rock_paper_scissors()

    doctest.testmod()


if __name__ == "__main__":
    main()

"""
Components of computational thinking  (decomposition, pattern matching, abstraction, algorithms) used in this script:
Decomposition was used to create the 3 check_X()'s and check_guess_is_valid()
Algorithms were used to in the 3 check_X()'s and check_guess_is_valid().
By creating the check_X() functions we employed abstraction.
"""
