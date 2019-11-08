import random


def combat_round(player_1: dict, player_2: dict):
    """
    Execute a round of combat.

    :param player_1: dictionary
    :param player_2: dictionary
    :precondition: player_1 has structure {Name, Dexterity, Class, HP {Max, Current}, Attacks[]}
    :precondition: player_2 has structure {Name, Dexterity, Class, HP {Max, Current}, Attacks[]}
    :postcondition: players will fight a single combat round
    """
    # by making a list I can code one set of fight instructions and then just flip the bits!
    player_list = [player_1, player_2]
    roles = {'attacker': 0, 'defender': 1}  # Assume player 1 attacks first

    if not does_p1_attack_first():
        swap_attacker_defender(roles)

    for i in range(0, 2):
        print(player_list[roles['attacker']]['Name'], "attacks with",
              choose_attack(player_list[roles['attacker']]['Attacks']))
        attack_success = attempt_attack(roll_die(1, 20), player_list[roles['attacker']]['Dexterity'])

        # calculate damage
        dmg_done = calculate_dmg(attack_success)

        # output an exclamation
        print(zounds(dmg_done))

        # apply damage
        player_list[roles['defender']]['HP']['Current'] = player_list[roles['defender']]['HP']['Current'] - dmg_done

        # see if defender lives
        if int(player_list[roles['defender']]['HP']['Current']) <= 0:
            print(player_list[roles['attacker']]['Name'], "is victorious!")
            print(doom(player_list[roles['defender']]['Name']))
            break
        else:  # flip the indices so the other player attacks
            swap_attacker_defender(roles)


def single_roll(number_of_sides: int) -> int:
    """
    Execute a single die roll.

    :param number_of_sides: int
    :precondition: number_of_sides > 0
    :postcondition: a random integer [1, number_of_sides]
    :return: int
    """

    return random.randint(1, number_of_sides)


def roll_die(number_of_rolls: int, number_of_sides: int) -> int:
    """
    Calculate sum of  die rolls.

    :param number_of_rolls: int
    :param number_of_sides: int
    :precondition: number_of_rolls [1, 3]
    :precondition: number_of_sides > 0
    :postcondition: calculate the sum of all the rolls
    :return: int
    >>> roll_die(0, 1)
    0
    >>> roll_die(1, 0)
    0
    """

    invalid_arg = False

    # Check both arguments, either one of them being 0 should return a 0
    if number_of_rolls == 0:
        invalid_arg = True

    if number_of_sides == 0:
        invalid_arg = True

    # If both arguments are > 0, roll and sum
    if invalid_arg:
        roll_sum = 0
    else:
        roll_sum = 0

        for i in range(0, number_of_rolls):
            roll_sum = roll_sum + single_roll(number_of_sides)

    return roll_sum


def attempt_attack(attack_roll: int, dexterity: int) -> bool:
    """
    Determine if an attack is successful
    :param attack_roll: int
    :param dexterity: int
    :precondition: both parameters must be integers
    :precondition: both parameters must be > -1
    :postcondition: determine whether or not an attack was successful
    :return: boolean

    >>> attempt_attack(1, 5)
    False
    >>> attempt_attack(5, 1)
    True
    >>> attempt_attack(8, 8)
    False
    """

    if attack_roll > dexterity:
        return True
    else:
        return False


def calculate_dmg(a_hit: bool) -> int:
    """
    Calculates damage done in an attack.

    :param a_hit: boolean
    :precondition: success is true or false
    :postcondition: the amount of damage applied is calculated
    :return: int
    """
    if a_hit:
        return roll_die(1, 6)
    else:
        return 0


def zounds(dmg_done: int) -> int:
    """
    Provide a rousing exclamation for a player's hit.

    :param dmg_done: int
    :precondition: a_hit is an int
    :precondition: a_hit >= 0
    :postcondition: an exclamation randomly selected, appropriate to the hit success is provided.
    :return: string
    """

    hit_list = ['Zounds! ', 'Wow! ', 'A crashing blow! ', 'A vicious attack! ', 'A brilliant strike! ',
                "I'm glad I'm not them! ", "Ka-blamm-o!!! "]

    miss_list = ["A miss!", "Airball!", "Whooooosh!", "A brilliant defence!", "Parried!",
                 "Were you even aiming at them?", "Defended!", "Nope."]

    if dmg_done > 0:
        return random.choice(hit_list) + str(dmg_done) + " damage done!"
    else:
        return random.choice(miss_list)


def doom(name: str) -> str:
    """
    Provide a rousing exclamation for a player's death.

    :param name: string
    :postcondition: a random mournful message is created
    :return: string
    """

    doom_list = ["The life is leaving " + name, "Light the fires of Ka-bloom! " + name + " is coming!", "OOOOOOOH " +
                 name, "Yikes! Look at the bones!!!!", "The deities will guide " + name + " to their rest",
                 name + ": You dead."]

    return random.choice(doom_list)


def does_p1_attack_first() -> bool:
    """
    Determine is p1 has the initiative to attack.

    :return: boolean
    """

    # Determine who attacks first
    p1_initiative = 0
    p2_initiative = 0

    while p1_initiative == p2_initiative:
        p1_initiative = roll_die(1, 20)
        p2_initiative = roll_die(1, 20)

    if p1_initiative > p2_initiative:
        return True
    else:
        return False


def choose_attack(attacks: list) -> str:
    """
    Choose the character's attack.

    :param attacks: list
    :precondition: list contains strings of attack types
    :postcondition: a random attack from attacks is selected
    :return: string
    """

    return random.choice(attacks)


def swap_attacker_defender(player_roles: dict):
    """
    Swap who the attacker and defender are.

    :param player_roles: dictionary
    :precondition: roles has structure {'attacker': [1,0], 'defender': [1,0]}
    :precondition: role values are mutually exclusive
    :postcondition: values of roles['attacker'] and roles['defender'] are switched

    >>> swap_attacker_defender({'attacker': 1, 'defender': 0})
    {'attacker': 0, 'defender': 1}
    >>> swap_attacker_defender({'attacker': 0, 'defender': 1})
    {'attacker': 1, 'defender': 0}
    """

    if player_roles['attacker'] == 1:
        player_roles['attacker'] = 0
        player_roles['defender'] = 1
    elif player_roles['attacker'] == 0:
        player_roles['attacker'] = 1
        player_roles['defender'] = 0
