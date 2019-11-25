def find_max_value_in_a_dictionary(d: dict, l: list) -> int:
    """
    Find the highest value in a sub-section of a dictionary.

    :param d: dictionary
    :param l: list
    :precondition: l's values must be in keys in d
    :postcondition: the highest value in the sub-section of d, defined by the keys as specified in l, is determined

    :return: int

    >>> find_max_value_in_a_dictionary({3: 6, 4: 5, 1:2, 9: 18, 12: 2}, [3, 4, 1])
    6
    """

    try:
        return max([v for k, v in d.items() if k in l])
    except ValueError:
        raise ValueError("At least one key in d must exist in l")


def find_first_key_of_a_value(val: int, d: dict) -> str:
    """
    Find the key for the first instance of a value in a dictionary.

    :param val: int, the value to look for
    :param d: dictionary, the dictionary to look through
    :precondition: val must exist in d
    :precondition: values in d must in integers
    :postcondition: the first dictionary key with the given value in the dictionary is given
    :return: str

    >>> find_first_key_of_a_value(1, {'apple': 5, 'cherry': 1, 'koala': 1, 'rhubarb': 7})
    'cherry'
    """

    for k, v in d.items():
        if v == val:
            return k

    raise IndexError("Variable, val, must be a key in dictionary, d")


def turn_bars_into_time(l: list, d: dict) -> str:
    """
    Print the time based on the number of bars making up the digital time of each digit

    :param l: list, # of bars representing the digits of a specific time on a digital clock
    :param d: dictionary,
    :precondition: 3 <= len(l) <= 4
    :precondition: l's structure is [<10's hour>, <1's hour>, :, <10's minute>, <1's minute>]
    :precondition: l values must be values in d

    :return: string

    >>>turn_bars_into_time([1, 3, 2, 4], {1: 1, 5: 2, 3: 0, 9: 4}
    "10:59"
    """

    time = ""
    time_list = []
    l.insert(-2, ":")

    for item in l:
        # time_list.append(find_first_key_of_a_value(item, d))
        if item != ':':
            time = time + str(find_first_key_of_a_value(item, d))
        else:
            time = time + ":"

    # time_list.insert(-2, ":")  # Do this at the the end so that a 1-digit vs. 2-digit hour doesn't interfere
    # return ''.join(time_list)
    return time


def im_not_sleepy() -> str:
    """
    Calculate the time requiring the most amount of bars on a digital clock.

    :postcondition: the time needing the most amount of bars, and the most bars is given
    :return: string

    >>> im_not_sleepy()
    10:08, 21
    """
    max_bars = []

    time_bars = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
    digit_possibilities = {'hour_tens': [1], 'hour_ones': [0, 1, 2, 4, 5, 6, 7, 8, 9],
                           'minute_tens': [0, 1, 2, 3, 4, 5], 'minute_ones': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]}

    # The number of minutes in the ones isn't affected by what comes after, so, just find it's biggest bar-value
    max_bars.insert(0, max(time_bars.values()))  # Instead of append() just for parallelism

    # Same thing for the 10's-minute
    max_bars.insert(0, find_max_value_in_a_dictionary(time_bars, digit_possibilities['minute_tens']))

    # Four hours: is any valid 2-digit hour more lines than the highest valid single digit?
    single_dgt_hr_bars = find_max_value_in_a_dictionary(time_bars, digit_possibilities['hour_ones'])

    # In 2-digit hours, the highest digit in the ten's position is 1 and the highest in the one's position is 2
    two_dgt_hr_bars = find_max_value_in_a_dictionary(time_bars, digit_possibilities['hour_tens']) \
                      + find_max_value_in_a_dictionary(time_bars, [0, 1, 2])

    if two_dgt_hr_bars > single_dgt_hr_bars:
        max_bars.insert(0, find_max_value_in_a_dictionary(time_bars, [0, 1, 2]))
        max_bars.insert(0, find_max_value_in_a_dictionary(time_bars, digit_possibilities['hour_tens']))
    else:
        max_bars.insert(0, single_dgt_hr_bars)

    bar_sum = sum(max_bars)

    # Now build the time string
    time = turn_bars_into_time(max_bars, time_bars)

    return "The time with the highest bars is " + time + " The number of bars is " + str(bar_sum)
