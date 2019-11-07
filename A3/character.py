
def determine_health_gain(current_health, max_health):
    """
    Calculate health that character gains.

    :param current_health: int
    :param max_health: int
    :precondition: current_health > 0
    :precondition: max_health > 0
    :precondition: current_health is int
    :precondition: max_health is int
    :postcondition: health restored to player is calculated, not to exceed max_health
    :return: int

    >>>determine_health_gain(1, 4)
    2
    >>>determine_health_gain(4, 4)
    0
    >>>determine_health_gain(5, 4)
    0
    """

    health_difference = max_health - current_health

    if health_difference >= 2:
        return 2
    elif health_difference == 1:
        return 1
    else:
        return 0


def create_character():
    """
    Create a character for use in the sud

    :postcondition: a character with limited DnD traits is created for use in the BCIT sud
    :return: dictionary

    >>>create_character()
    {'Name': 'Anonymous', 'Dexterity': 0, 'Class': 'student', 'HP': {'Current': 10, 'Max': 10}},
    'Attacks': ['studiousness', 'hard work', 'collaboration', 'academic integrity'], 'x-coord': 0, 'y-coord': 0}
    """

    character = {'Name': 'Anonymous', 'Dexterity': 10, 'Class': 'student', 'HP': {'Current': 10, 'Max': 10},
                 'Attacks': ['studiousness', 'hard work', 'collaboration', 'academic integrity'],
                 'x-coord': 0, 'y-coord': 0}

    return character
