import random


def generate_monster_name():
    """
    Generate a monster name.

    :postcondition: a name randomly chosen from a list of possibilities is picked
    :return: string
    """

    possible_names = ('Chris', 'Sam', 'Neda', 'Takashi', 'Amir')

    return possible_names[random.randint(0, len(possible_names))]


def get_monster_attacks(name):
    """
    Provide attacks for the monster, specific to the monster.

    :param name: string
    :precondition: name is a legal monster name, supplied by generate_monster_name()
    :postcondition: regular attacks + monster-specific attacks are provided
    :return: list
    """
    attacks = ['quiz', 'assignment', 'midterm']

    if name == 'Chris':
        attacks.extend(['partner quiz', 'python', 'question when you were trying to hide'])
    elif name == 'Sam':
        attacks.extend(['comma splice'])
    elif name == 'Takashi':
        attacks.extend(['miniquiz', 'donut', 'number system'])
    elif name == 'Neda':
        attacks.extend(['git', 'figma', 'bootstrap'])
        attacks.remove('midterm')
    elif name == 'Amir':
        attacks.extend(['fake quiz', 'zombie attack'])

    return attacks


def generate_monster():
    """
    Create a monster in the dungeon.

    :postcondition: a fully-formed, ready to fight monster is created.
    :return: dictionary
    """

    monster = {'Name': generate_monster_name(), 'Attacks': get_monster_attacks(), 'HP': {'Current': 5, 'Max': 5},
               'Dexterity': 0, 'Class': 'sud'}

