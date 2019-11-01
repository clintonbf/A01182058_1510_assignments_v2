# import dungeonsanddragons

# Defining two constants for the size of the game board, so we can elegantly change it
import random

MAX_X = 5
MAX_Y = 5


def create_dungeon():
    """
    Create a X x Y dungeon.

    :postcondition: a single-level dungeon (MAX_X x MAX_Y) is created
    :return: list
    """

    game_board = []

    for x in range(MAX_X):
        game_row = [[x, y] for y in range(MAX_Y)]
        game_board.append(game_row)

    return game_board


def execute_movement(location, direction):
    """
    Move one space on the board

    :param location: list
    :param direction: int
    :precondition: current_spot is a 2-element list
    :precondition: 0 >= elements in current_spot <= 4
    :precondition: 1 >= direction <= 4
    :postcondition: will generate co-ordinates for where the player moved to
    :return: 2-element list

    >>>execute_movement([1, 2], 1)
    [1, 3]
    >>>execute_movement([1, 5], 1)
    [1, 5]
    >>>execute_movement([1, 2], 3)
    [2, 2]
    """

    new_x = location[0]
    new_y = location[1]

    if direction == 1 and location[1] < MAX_Y:  # ie. north
        new_y += 1
    elif direction == 2 and location[1] > 0:  # ie. south
        new_y -= 1
    elif direction == 3 and location[0] < MAX_X:  # ie. east
        new_x += 1
    elif direction == 4 and location[0] > 0:  # ie. west
        new_x -= 1

    return [new_x, new_y]


def is_monster_encountered():
    """
    Determine if a monster is encountered.

    :postcondition: whether or not a monster is encountered
    :return: bool
    """

    found = random.randint(1, 4)
    # found = dungeonsanddragons.roll_die(1, 4)

    if found == 1:
        return True
    else:
        return False

