def find_max_bar_in_a_group(d: dict, l: list) -> int:
    """
    Find the number with the highest amount of bars in a group
    :param d: dictionary
    :param l: list
    :precondition: l has no other values than what is contained in d
    :postcondition: find the value in l that has the most amount of lines representing it

    :return: int

    >>> find_max_bar_in_a_group({3: 6, 4: 4, 1:2}, [3, 4, 1])
    3
    """
    temp_dict = {k: v for k, v in d.items() if k in l}

    return max(temp_dict.values())


def im_not_sleepy() -> str:
    """
    Calculate the time requiring the most amount of bars on a digital clock.

    :postcondition: the time needing the most amount of bars, and the most bars is given
    :return: string

    >>> im_not_sleepy()
    10:08, 21
    """
    max_bars = []

    time_bars = {0: 6, 1: 2, 2: 6, 3: 6, 4: 4, 5: 6, 6: 6, 7: 3, 8: 7, 9: 6}
    digit_possibilities = {'hour_tens': [1], 'hour_ones': [0, 1, 2, 4, 5, 6, 7, 8, 9],
                           'minute_tens': [0, 1, 2, 3, 4, 5], 'minute_ones': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]}

    # The number of minutes in the ones isn't affected by what comes after, so, just find it's biggest
    max_bars.append(max(time_bars.values()))

    # By the same token, the biggest 10's minutes is just whatever is the biggest within its own set
    max_bars.append(find_max_bar_in_a_group(time_bars, digit_possibilities['minute_tens']))

    # The hours is tricky because we can have a single digit hour OR we can have a 2-digit
    # The question is: is any valid 2-digit hour more lines than the highest valid single digit?
    highest_single_digit_hour = find_max_bar_in_a_group(time_bars, digit_possibilities['hour_ones'])

    # In 2-digit hours, the highest digit in the ten's position is 1 and the highest in the one's position is 2
    bars_in_a_two_digit_hour = time_bars[digit_possibilities['hour_tens'][0]] + time_bars[2]

    max_bars.append(bars_in_a_two_digit_hour) if bars_in_a_two_digit_hour > highest_single_digit_hour else max_bars.append(highest_single_digit_hour)

    return "The number of bars is " + str(sum(max_bars))


def main():
    print(im_not_sleepy())


if __name__ == '__main__':
    main()
