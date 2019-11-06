import random


def single_roll(number_of_sides):
    """
    Execute a single die roll.

    :param number_of_sides: int
    :precondition: number_of_sides > 0
    :postcondition: a random integer [1, number_of_sides]
    :return: int
    """

    return random.randint(1, number_of_sides)


# noinspection DuplicatedCode
def roll_die(number_of_rolls, number_of_sides):
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


def print_inventory(itemization_list, inv_list):
    """
    Print a list of store inventory.

    :param itemization_list: list of strings
    :param inv_list: list of strings
    :precondition: itemization_list is a list of strings
    :precondition: inv_list is a list of strings of the same size as itemization list
    :postcondition: a list (of strings) is output, combining the two parameters
    :return: nothing

    >>> print_inventory(['1', '2', '3'], ['a', 'b', 'c'])
    1a
    2b
    3c
    """
    for i in range(0, len(inv_list)):
        print(itemization_list[i] + inv_list[i])


def choose_inventory():
    """
    Provide a shopping experience for the user.

    :return: list of strings
    """

    gear_list = ["Rapier", "Broadsword", "Vorpal sword", "The constrictor", "A duck!", "giant spoon", "icingdeath",
                 "bag of holding", "boomstick", "stabstick", "greaves", "gambeson", "vambraces", "wand of fire",
                 "Twinkle", "Cucumber salad"]
    visual_gear_numbering = []

    for i in range(0, len(gear_list)):
        visual_gear_numbering.append(str(i + 1) + ". ")

    shopping_bag = []

    print("Welcome to Treehorn Hessia's Emporium of Great Adventuring Products!\n"
          "Looking at you, I'm going to be able to retire.\n"
          "What would you like (Choose -1 to complete your purchase)?")

    print_inventory(visual_gear_numbering, gear_list)

    still_shopping = True

    while still_shopping:
        choice = int(input())

        if choice in range(0, (len(gear_list) + 1)):
            user_choice = choice - 1
            shopping_bag.append(gear_list[user_choice])

            print("Excellent choice!")
            print("What's next?")
            print_inventory(visual_gear_numbering, gear_list)
        elif choice == -1:
            still_shopping = False

            print("Thanks for shopping with us; here's what you've purchased")

            for i in range(0, len(shopping_bag)):
                print(shopping_bag[i])
        else:
            print("Sorry, we don't sell that.")
            print("What would you like to purchase?")
            print_inventory(visual_gear_numbering, gear_list)

    return shopping_bag


def generate_vowel():
    """
    Return a randomly-selected vowel (incl. y).

    :postcondition: single vowel randomly selected
    :return: string
    """
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']

    which_vowel = random.choice(vowels)

    return which_vowel


def generate_consonant():
    """
     Return a randomly-selected consonant (incl. y).

    :postcondition: single consonant randomly selected
    :return: string
    """
    consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y',
                 'z']

    return random.choice(consonant)


def generate_syllable():
    """
    Generate a consonant-vowel pair

    :postcondition: consonant-vowel pair created
    :return: string
    """

    return generate_consonant() + generate_vowel()


def generate_name(syllables):
    """
    Generate string of consonant-vowel pairs.

    :param syllables: int, > 0
    :precondition: syllables is an int, > 0
    :postcondition: generates a syllables consonant-vowel pairs of length 2 * syllables
    :return: string
    """

    name = ""

    for i in range(0, syllables):
        name = name + generate_syllable()

    return name.title()


def select_race():
    """
    Ask a user to select a DnD race from a possible list.

    :postcondition: a player race is selected
    :return: string
    """

    race_list = ['', 'dragonborn', 'dwarf', 'elf', 'gnome', 'half-elf', 'halfling', 'half-orc', 'human', 'tiefling']

    print("Choose a race from the list of possibilities (select via number):")
    for i in range(1, len(race_list)):
        print(str(i) + ". " + race_list[i])

    race = input()

    return race_list[int(race)].lower()


def select_class():
    """
    Ask a user to select a DnD class from a possible list.

    :postcondition: a player class is selected
    :return: string
    """

    class_list = ['', 'barbarian', 'bard', 'cleric', 'druid', 'fighter', 'monk', 'paladin', 'ranger', 'rogue',
                  'sorcerer', 'warlock', 'wizard']

    chosen_class = input("Choose a class from the list of possibilities (select via number):\n"
                         "1. barbarian\n"
                         "2. bard\n"
                         "3. cleric\n"
                         "4. druid\n"
                         "5. fighter\n"
                         "6. monk\n"
                         "7. paladin\n"
                         "8. ranger\n"
                         "9. rogue\n"
                         "10. sorcerer\n"
                         "11. warlock\n"
                         "12. wizard\n"
                         )

    return class_list[int(chosen_class)].lower()


def calculate_hp(player_class):
    """
    Generate a player's starting HP

    :precondition: player_class is a string
    :precondition: player_class is a legal DnD character class
    :postcondition: player_class' starting hit points
    :param player_class: string
    :return: int
    """

    if player_class.lower() in ["barbarian"]:
        return roll_die(1, 12)
    elif player_class.lower() in ["fighter", "paladin", "ranger"]:
        return roll_die(1, 10)
    elif player_class.lower() in ["bard", "cleric", "druid", "monk", "rogue", "warlock"]:
        return roll_die(1, 8)
    elif player_class.lower() in ["sorcerer", "wizard"]:
        return roll_die(1, 6)
    elif player_class.lower() in ["monster", "student"]:
        return roll_die(1, 6)


def create_character(name_length):
    """
    Generate a DnD character.

    :param name_length: int
    :precondition: name_length is int, > 0
    :postcondition: DnD character with a name & attributes (8 elements)
    :return: dictionary
    """

    the_character = {'Name': generate_name(name_length), 'Race': select_race(), 'Class': select_class()}

    hp = calculate_hp(the_character['Class'])  # die roll
    the_character['HP'] = {'Max': hp, 'Current': hp}

    # create our attributes
    att_list = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]

    for i in range(0, len(att_list)):
        the_character[att_list[i]] = roll_die(3, 6)  # die roll * 6

    the_character['XP'] = 0
    the_character['Inventory'] = {}

    return the_character


def print_character(character):
    """
    Output DnD character details.

    :param character: list
    :precondition: a character list generated by create_character()
    :postcondition: output about your amazing character
    :return: none
    """

    print("Here's what you need to know about me!")

    for attribute in ['Name', 'Race', 'Class', 'XP']:
        print(attribute + ": " + str(character[attribute]))

    # Now print HPs
    print("Max HP: " + str(character['HP']['Max']))
    print("Current HP: " + str(character['HP']['Current']))

    # Lastly, inventory
    print("My gear!")
    gear_list = character["Inventory"]
    visual_gear_numbering = []

    for i in range(0, len(gear_list)):
        visual_gear_numbering.append(str(i + 1) + ". ")

    print_inventory(visual_gear_numbering, gear_list)


def attempt_attack(attack_roll, dexterity):
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


def calculate_dmg(a_hit, char_class):
    """
    Calculates damage done in an attack.

    :param a_hit: boolean
    :param char_class: string
    :precondition: success is true or false
    :precondition: attacker's class is as defined in select_class()
    :postcondition: the amount of damage applied, based on success
    :return: int
    """
    if a_hit:
        return calculate_hp(char_class)
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


def does_p1_attack_first():
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


def choose_attack(attacks):
    """
    Choose the character's attack.

    :param attacks: list
    :precondition: list contains strings of attack types
    :postcondition: a random attack from attacks is selected
    :return: string
    """

    return random.choice(attacks)


# TODO: add in code to include what the monster attacked with
def combat_round(player_1, player_2):
    """
    Execute a round of combat.

    :param player_1: dictionary
    :param player_2: dictionary
    :precondition: player_1 has structure {Name, Dexterity, Class, HP {Max, Current}, attacks[]}
    :precondition: player_2 has structure {Name, Dexterity, Class, HP {Max, Current}, attacks[]}
    :postcondition: players will fight a single combat round
    """
    # by making a list I can code one set of fight instructions and then just flip the bits!
    player_list = [player_1, player_2]

    p1_init = does_p1_attack_first()

    # Set the indices for who attacks first. We'll swap these after (unless there's a killing blow)
    if p1_init:
        px = 0
        py = 1
    else:
        px = 1
        py = 0

    print(player_list[px]['Name'] + " attacks first!")
    print(player_list[px]['Name]'], "attacks with a(n)", choose_attack(player_list[px]['Attacks']))

    for i in range(0, 2):
        print(player_list[px]['Name'] + " attacks!")
        attack_success = attempt_attack(roll_die(1, 20), player_list[px]['Dexterity'])

        # calculate damage
        dmg_done = calculate_dmg(attack_success, player_list[px]['Class'])

        # output an exclamation
        print(zounds(dmg_done))

        # apply damage
        player_list[py]['HP']['Current'] = player_list[py]['HP']['Current'] - dmg_done

        # see if py lives
        if int(player_list[py]['HP']['Current']) <= 0:
            print(doom(player_list[py]['Name']))
            break
        else:  # flip the indices so the other player attacks
            if px == 0:
                px = 1
                py = 0
            else:
                px = 0
                py = 1


def wait_for_continue(bln):
    """
    Waits for user to enter a key.

    :param bln: boolean
    :return:

    >>> wait_for_continue(True)

    >>> wait_for_continue(False)

    """
    if bln:
        input("Press enter key to continue")
    else:
        pass


def main():
    print("Initing the Doom refresh daemon..............")

    pausing = ""
    while pausing not in ["y", "n"]:
        pausing = input("Do you want pausing (y/n)?")

    if pausing == "y":
        pausing = True
    else:
        pausing = False

    print("\nPlayer 1! Come forward")
    p1 = create_character(3)
    print("\n##########Welcome " + p1['Name'] + "##########\n")

    wait_for_continue(pausing)

    print("//////////Let's go shopping!//////////\n")
    p1['Inventory'] = choose_inventory()

    wait_for_continue(pausing)

    print("\n%%%%%%%%%%Announce yourself!%%%%%%%%%%\n")
    print_character(p1)

    wait_for_continue(pausing)

    print("\nPlayer 2! Come forward")
    p2 = create_character(4)

    print("\n**********Welcome " + p2['Name'] + "**********\n")

    print("\n//////////Let's go shopping!//////////")
    p2['Inventory'] = choose_inventory()

    wait_for_continue(pausing)

    print("\n%%%%%%%%%%Announce yourself!%%%%%%%%%%\n")
    print_character(p2)

    wait_for_continue(pausing)

    print("\n\nOur matchup is: " + str(p1['Name']) + "(" + str(p1['HP']['Current']) + ")" + " and " + str(
        p2['Name']) + "(" + str(p2['HP']['Current']) + ")")

    print("\n**********Players! Engage in holy combat**********\n\n")

    wait_for_continue(pausing)

    combat_round(p1, p2)


if __name__ == '__main__':
    main()
