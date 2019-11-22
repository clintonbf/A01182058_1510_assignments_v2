def denomination_count(amount: float, denomination: float) -> int:
    """
    Calculate the amount of a certain denomination that can represent a number.

    :param amount: float
    :param denomination: float
    :postcondition: the number of times that denomination divides into amount is calculated
    :return: int

    >>>denomination_count(100, 100)
    1
    >>>denomination_count(66.53, 50)
    1
    >>>denomination_count(11.11, 11.11)
    1
    >>>denomination_count((10, .01)
    1000
    """
    pass


def cash_money(amount: float) -> dict:
    """
    Convert an amount of money into the fewest amount of bills and coins to represent it.

    :param amount: float
    :precondition: amount >= 0
    :precondition: amount is a float
    :postcondition: amount is broken down into the fewest amount of bills and coins that represent it
    :return: dictionary

    >>>cash_money(66.53)
    {50: 1, 10: 1, 5: 1, 1: 1, 0.25: 2, 0.01: 3}
    """

    denominations = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0, .25: 0, .1: 0, .5: 0, .01: 0}

    if not isinstance(amount, float):
        raise TypeError("amount must be a float")

    if amount < 0:
        raise ValueError("amount must be > 0")

    cash_breakdown = {}

    for denomination in denominations:
        denominations[denomination] = amount // denomination
        amount -= amount * denomination

    return {k: v for k, v in denominations.items if denominations[k] > 0}
