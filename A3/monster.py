import random


def generate_monster_name():
    """
    Generate a monster name.

    :postcondition: a name randomly chosen from a list of possibilities is picked
    :return: string
    """

    possible_names = ('Chris', 'Sam', 'Neda', 'Takashi', 'Amir')

    return possible_names[random.randint(0, len(possible_names))]
