import random

from A3.character import create_character, determine_health_gain
from A3.monster import spawn_monster


def get_max_x() -> int:
    """
    Provide constant value for x.

    :postcondition: value for constant x is provided
    :return: int

    >>>get_max_x()
    5
    """
    return 5


def get_max_y() -> int:
    """
        Provide constant value for x.

        :postcondition: value for constant x is provided
        :return: int

    >>> get_max_y()
    5
    """
    return 5


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


# noinspection DuplicatedCode
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


def calculate_dmg(a_hit):
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


def zounds(dmg_done):
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


def doom(name):
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


def execute_movement(location, direction):
    """
    Move one space on the board

    :param location: list
    :param direction: int
    :precondition: current_spot is a 2-element list
    :precondition: 0 >= elements in current_spot <= 4
    :precondition: 1 >= choice <= 4
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

    if direction == 1 and location[1] < get_max_y():  # ie. north
        new_y += 1
    elif direction == 2 and location[1] > 0:  # ie. south
        new_y -= 1
    elif direction == 3 and location[0] < get_max_x():  # ie. east
        new_x += 1
    elif direction == 4 and location[0] > 0:  # ie. west
        new_x -= 1

    return [new_x, new_y]


def get_movement() -> str:
    """
    Get movement choice from user.

    :postcondition: movement choice obtained
    :return: string
    """

    return input("Which choice do you want to go (n, s, e, w)? Type 'quit' to... quit")


def validate_choice(choice: str, valid_choices: tuple) -> bool:
    """
    Validate users movement choice.

    :param valid_choices: tuple
    :param choice: string
    :precondition: valid_choices are strings
    :precondition: valid_choices contains the valid choices to check against
    :return: bool

    >>>validate_choice('n', ('n', 's', 'w', 'e'))
    True
    >>>validate_choice('1', ('n', 's', 'w', 'e'))
    False
    >>>validate_choice('north', ('n', 's', 'w', 'e'))
    False
    >>>validate_choice('g', ('n', 's', 'w', 'e'))
    False
    """

    if choice.lower() in valid_choices:
        return True
    else:
        return False


def advise_of_movement_error(error: int):
    """
    Notify user they made an invalid movement.

    :param error: int
    :precondition: error is 1 if invalid movement option was provided
    :precondition: error is 2 if user hit a wall
    :postcondition: a helpful message is produced

    >>>advise_of_movement_error(1)
    "Invalid movement option. Please enter again (n, s, w, e)"
    >>>advise_of_movement_error(2)
    "You hit a wall; ouch. Try a different choice(n, s, w, e)"
    """

    if error == 1:
        print("Invalid movement option. Please enter again (n, s, w, e)")
    elif error == 2:
        print("You hit a wall; ouch. Try a different choice(n, s, w, e)")


def did_user_hit_a_wall(direction: str, character: dict) -> bool:
    """
    Determine if user hit a wall when moving.

    :param direction: string
    :param character: dictionary
    :precondition: choice is a single character in [n, s, w, e]
    :precondition: character is a dictionary
    :precondition: character contains key "x-coord"
    :precondition: character contains key "y-coord"
    :precondition: -1 > x-coord < 5
    :precondition: -1 > y-coord < 5
    :postcondition: determine whether valid movement choice ran into a wall
    :return: bool

    >>>did_user_hit_a_wall('n', {'x-coord': 0, 'y-coord': 3})
    False
    >>>did_user_hit_a_wall('n', {'x-coord': 0, 'y-coord': 0})
    True
    >>>did_user_hit_a_wall('e', {'x-coord': 4, 'y-coord': 3})
    True
    >>>did_user_hit_a_wall('e', {'x-coord': 0, 'y-coord': 3})
    False
    """

    if direction == 'n':
        if character['y-coord'] == 0:
            return True
        else:
            return False
    elif direction == 's':
        if character['y-coord'] == 4:
            return True
        else:
            return False
    elif direction == 'e':
        if character['x-coord'] == 4:
            return True
        else:
            return False
    elif direction == 'w':
        if character['x-coord'] == 0:
            return True
        else:
            return False


def move_char(direction: str, character: dict):
    """
    Move the character to a new location.

    :param character: dictionary
    :param direction: string
    :precondition: choice is a single character in [n, s, w, e]
    :precondition: character is a dictionary
    :precondition: character contains key "x-coord"
    :precondition: character contains key "y-coord"
    :precondition: -1 > x-coord < 5
    :precondition: -1 > y-coord < 5
    :postcondition: updates character's position

    >>>move_char('s',  {'x-coord': 0, 'y-coord': 0})
    {'x-coord':0, 'y-coord': 1}
    >>>move_char('e', {'x-coord': 0, 'y-coord': 3})
    {'x-coord':1, 'y-coord': 3}
    """

    if direction == 'n':
        character['y-coord'] -= 1
    elif direction == 's':
        character['y-coord'] += 1
    elif direction == 'e':
        character['x-coord'] += 1
    elif direction == 'w':
        character['x-coord'] -= 1


def is_monster_encountered() -> bool:
    """
    Determine if a monster is encountered.

    :postcondition: whether or not a monster is encountered
    :return: bool
    """

    found = roll_die(1, 4)

    if found == 1:
        return True
    else:
        return False


def stab_in_the_back() -> bool:
    """
    Attempt a stab in the back.

    :postcondition: determine whether or not a successful stab in the back occurred
    :return: bool
    """

    if roll_die(1, 10) == 1:
        return True
    else:
        return False


def process_cheap_shot() -> int:
    """
    Calculate damage from cheap shot.

    :postcondition: calculate how much damage is executed from a stab in the back
    :return: int
    """

    if stab_in_the_back():
        return roll_die(1, 4)
    else:
        return 0


def play_game():
    """
    Play 'Trapped at BCIT'.

    :postcondition: you are filled with joy and delight
    :postcondition: hours have passed
    """

    player = create_character()

    print("You find yourself at BCIT DTC on the 6th floor! Try to escape.")

    while player['HP']['Current'] > 0:
        movement = get_movement()

        if movement.lower() == 'quit':
            print("k bye. But don't think this means you've escaped!")
            break

        # Ensure movement is valid
        while not validate_choice(movement, ('n', 's', 'w', 'e')):
            advise_of_movement_error(1)
            movement = get_movement()

        # Did you walk into a wall?
        if did_user_hit_a_wall(movement, player):
            advise_of_movement_error(2)
        else:
            move_char(movement, player)

            # Heal (if possible) and output new health
            player['HP']['Current'] += determine_health_gain(player['HP']['Current'], player['HP']['Max'])
            print("Current HP:", player['HP']['Current'])

            if is_monster_encountered():
                monster = spawn_monster()
                print(monster['Name'], "appears, with a need to evaluate in their eyes! You have no time for this!"
                                       "(Or do you?)")

                fight_or_flight = input("So, what's the deal: fight (choose 'y') or flight (choose 'n')?")
                while not validate_choice(fight_or_flight, ('y', 'n')):
                    fight_or_flight = input("Sorry, you gotta choose to fight ('y') or flee ('n')")

                if fight_or_flight == 'y':
                    while player['HP']['Current'] > 0 and monster['HP']['Current'] > 0:
                        combat_round(player, monster)
                else:
                    # 10% change you're stabbed, damage 1d4
                    damage_taken = process_cheap_shot()
                    if damage_taken > 0:
                        print(monster['Name'], "notices your absence! That cost you", damage_taken, "hp!")
                        player['HP']['Current'] -= damage_taken

                if player['HP']['Current'] > 0:
                    print("You've managed to escape with", player['HP']['Current'], " hp. Let's hope you don't run into"
                                                                                    " another instructor anytime soon.")
                else:
                    print("You have been unable to cope with the workload. See you PTS.")


def main():
    play_game()


if __name__ == '__main__':
    main()
