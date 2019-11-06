import random


def generate_monster_name():
    """
    Generate a monster name.

    :postcondition: a name randomly chosen from a list of possibilities is picked
    :return: string
    """

    possible_names = ('Chris', 'Sam', 'Neda', 'Takashi', 'Amir')

    return random.choice(possible_names)


def get_monster_attacks(name):
    """
    Provide attacks for the monster, specific to the monster.

    :param name: string
    :precondition: name is a legal monster name, supplied by generate_monster_name()
    :postcondition: regular attacks + monster-specific attacks are provided
    :return: list
    """
    attacks = ['a quiz', 'an assignment', 'the midterm']

    if name == 'Chris':
        attacks.extend(['a partner quiz', 'a python', 'a question when you were trying to hide'])
    elif name == 'Sam':
        attacks.extend(['a comma splice'])
    elif name == 'Takashi':
        attacks.extend(['a miniquiz', 'a donut', 'a number system'])
    elif name == 'Neda':
        attacks.extend(['git', 'figma', 'bootstrap'])
        attacks.remove('midterm')
    elif name == 'Amir':
        attacks.extend(['a fake quiz', 'a zombie attack'])

    return attacks


def spawn_monster():
    """
    Create a monster in the dungeon.

    :postcondition: a fully-formed, ready to fight monster is created.
    :return: dictionary
    """

    monster = {'Name': generate_monster_name(), 'HP': {'Current': 5, 'Max': 5},
               'Dexterity': 10, 'Class': 'monster'}

    monster['Attacks'] = get_monster_attacks(monster['Name'])

    return monster
