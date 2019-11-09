def get_monster_chance() -> int:
    """
    Set the chance of encountering a monster.

    :postcondition: the number of sides of the rolled die is set.
    :return: int

    >>>get_monster_chance()
    4
    """

    return 4


def get_special_item_chance() -> int:
    """
    Get the chance of finding a special item.

    :postcondition: the number of sides of the rolled die is set.
    :return: int

    >>> get_special_item_chance()
    15
    """

    return 15


def get_find_the_stairs_chance() -> int:
    """
    Get the chance of finding a special item.

    :postcondition: the number of sides of the rolled die is set.
    :return: int

    >>> get_find_the_stairs_chance()
    10
    """

    return 10


def get_max_x() -> int:
    """
    Provide constant value for max x.

    :postcondition: value for constant x is provided
    :return: int

    >>>get_max_x()
    4
    """
    return 4


def get_max_y() -> int:
    """
        Provide constant value for max y.

        :postcondition: value for constant max y is provided
        :return: int

    >>> get_max_y()
    4
    """
    return 4


def get_min_x() -> int:
    """
    Provide constant value for min x.

    :postcondition: value for constant max x is provided
    :return: int

    >>>get_min_x()
    0
    """
    return 0


def get_min_y() -> int:
    """
    Provide constant value for min y.

    :postcondition: value for constant min y is provided
    :return: int

    >>>get_min_y()
    0
    """
    return 0


def get_extra_commands() -> tuple:
    """
    Provide extra commands.

    :postcondition: the additional valid commands are provided
    :return: tuple

    >>> get_extra_commands()
    ('help', 'god_exit', 'god_battle', 'god_stairs')
    """

    return_tuple = ('help', 'god_exit', 'god_battle', 'god_stairs', 'quit')

    return return_tuple


def get_valid_movement_choices() -> tuple:
    """
    Get the valid choices in movement.

    :postcondition: provide a tuple of the valid movement choices
    :return: tuple
    """

    valid_choices = ('n', 's', 'w', 'e')

    return valid_choices


def add_formatting_line():
    """
    Add a formatting line.

    :postcondition: readability is increased

    >>> add_formatting_line()
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
