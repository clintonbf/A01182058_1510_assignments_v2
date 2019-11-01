import doctest


def how_many_days(seconds):
    """
    Calculate how many days are comprised in the time provided.

    :param seconds: int
    :precondition: argument is an integer >= 0
    :postcondition: number of days comprised by the argument
    :return: int

    >>> how_many_days(86401)
    1
    """

    return seconds // 86400


def how_many_hours(seconds):
    """
    Calculate how many hours are comprised in the time provided.

    :param seconds: int
    :precondition: argument is an integer >= 0
    :postcondition: number of hours comprised by the argument
    :return: int

    >>> how_many_hours(7200)
    2
    """

    return seconds // 3600


def how_many_minutes(seconds):
    """
    Calculate how many minutes are comprised in the time provided.

    :param seconds: int
    :precondition: argument is an integer >= 0
    :postcondition: number of minutes comprised by the argument
    :return: int

    >>> how_many_minutes(180)
    3
    """

    return seconds // 60


def time_calculator(seconds):
    """
    Convert seconds into respective days, hours and minutes.

    :param seconds: integer
    :precondition: argument is an integer >= 0
    :postcondition: argument value converted to days, hours, seconds
    :return: string

    >>> time_calculator(980)
    We have 0 days, 0 hours, 16 minutes and 20 seconds
    """
    # 60 seconds in a minute
    # 3600 seconds in an hour
    # 86 400 seconds in a day

    hours = 0
    minutes = 0

    days = how_many_days(seconds)

    if days == 0:
        time_remaining = seconds
    else:
        time_remaining = seconds % 86400

    if time_remaining >= 3600:  # ie. there is at least 1 hour
        hours = how_many_hours(time_remaining)
        time_remaining = time_remaining % 3600

    if time_remaining >= 60:
        minutes = how_many_minutes(time_remaining)

    seconds = time_remaining % 60

    print("We have %d days, %d hours, %d minutes and %d seconds" % (days, hours, minutes, seconds))


def main():
    # print("TEST 60 (1 min)")
    # time_calculator(60)
    # print("TEST 3600 (1 hour)")
    # time_calculator(3600)
    # print("TEST 86400 (1 day)")
    # time_calculator(86400)
    # print("TEST ")
    # time_calculator(980)

    doctest.testmod()


if __name__ == "__main__":
    main()

"""
Components of computational thinking  (decomposition, pattern matching, abstraction, algorithms) used in this script:
Decomposition occurs in the separating out of the how_many_X functions.
The methodology behind determining how many of each unit of time (day, hour, minute, second) is an example of
    algorithmic thinking.

"""
