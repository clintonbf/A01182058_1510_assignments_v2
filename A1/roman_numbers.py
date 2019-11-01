import doctest


def convert_to_roman_ones(num):
    """
    Convert a decimal integer to Roman equivalent in the one's position
    :param num: int [0, 9]
    :precondition: 0 <= argument <= 9
    :postcondition: a Roman number between 0 - 9
    :return: string

    >>> convert_to_roman_ones(5)
    'V'
    """

    if num == 9:
        return_value = "IX"
    elif num == 8:
        return_value = "VIII"
    elif num == 7:
        return_value = "VII"
    elif num == 6:
        return_value = "VI"
    elif num == 5:
        return_value = "V"
    elif num == 4:
        return_value = "IV"
    elif num == 3:
        return_value = "III"
    elif num == 2:
        return_value = "II"
    elif num == 1:
        return_value = "I"
    else:
        return_value = ""

    return return_value


def convert_to_roman_tens(num):
    """
    Convert a decimal integer to Roman equivalent in the ten's position
    :param num: int [0, 9]
    :precondition: 0 <= argument <= 9
    :postcondition: a Roman number between 10 - 90
    :return: string

    >>> convert_to_roman_tens(4)
    'XL'
    """
    if num == 9:
        return_value = "XC"
    elif num == 8:
        return_value = "LXXX"
    elif num == 7:
        return_value = "LXX"
    elif num == 6:
        return_value = "LX"
    elif num == 5:
        return_value = "L"
    elif num == 4:
        return_value = "XL"
    elif num == 3:
        return_value = "XXX"
    elif num == 2:
        return_value = "XX"
    elif num == 1:
        return_value = "X"
    else:
        return_value = ""

    return return_value


def convert_to_roman_hundreds(num):
    """
    Convert a decimal integer to Roman equivalent in the hundred's position
    :param num: int [0, 9]
    :precondition: 0 <= argument <= 9
    :postcondition: a Roman number between 100 - 900
    :return: string

    >>> convert_to_roman_hundreds(7)
    'DCC'
    """
    if num == 9:
        return_value = "CM"
    elif num == 8:
        return_value = "DCCC"
    elif num == 7:
        return_value = "DCC"
    elif num == 6:
        return_value = "DC"
    elif num == 5:
        return_value = "D"
    elif num == 4:
        return_value = "CD"
    elif num == 3:
        return_value = "CCC"
    elif num == 2:
        return_value = "CC"
    elif int == 1:
        return_value = "C"
    else:
        return_value = ""

    return return_value


def convert_to_roman_thousands(num):
    """
    Convert a decimal integer to Roman equivalent in the thousand's position
    :param num: int [0, 9]
    :precondition: 0 <= argument <= 9
    :postcondition: a Roman number between 1000 - 9000
    :return: string

    >>> convert_to_roman_thousands(2)
    'MM'
    """
    if num == 9:
        return_value = "MMMMMMMMM"
    elif num == 8:
        return_value = "MMMMMMMM"
    elif num == 7:
        return_value = "MMMMMMM"
    elif num == 6:
        return_value = "MMMMMM"
    elif num == 5:
        return_value = "MMMMM"
    elif num == 4:
        return_value = "MMMM"
    elif num == 3:
        return_value = "MMM"
    elif num == 2:
        return_value = "MM"
    elif num == 1:
        return_value = "M"
    else:
        return_value = ""

    return return_value


def convert_to_roman_numeral(positive_int):
    """
    Convert a decimal integer to a Roman numeral.

    :param: positive_int, a positive integer
    :precondition: argument is a positive integer, [1, 10000]
    :postcondition: Roman numeral equivalent of the argument
    :returns: string

    >>> convert_to_roman_numeral(499)
    'CDXCIX'
    """
    start_string = str(positive_int)

    # analyze each digit position in the number and convert it appropriate to its position
    if len(start_string) == 5:
        conversion_string = "MMMMMMMMMM"  # Valid shortcut, since only 1 5-digit number is allowed (10 000)
    else:
        # the maximum number can be 9999
        tens = ""
        hundreds = ""
        thousands = ""

        # Now, this is a mouthful. We take the element of start_string in the index position =
        # ( len(start_string) - 1 ) which is the 0th element, the one's position. We then cast that as an int
        ones = convert_to_roman_ones(int(start_string[(len(start_string) - 1)]))

        # Extending the idea, we take the element of start string in the index position =
        # ( len(start_string) - 2) which is the 1st element, the 10's position. We cast that as an int
        if len(start_string) > 1:
            tens = convert_to_roman_tens(int(start_string[(len(start_string) - 2)]))

        if len(start_string) > 2:
            hundreds = convert_to_roman_hundreds(int(start_string[(len(start_string) - 3)]))

        if len(start_string) > 3:
            thousands = convert_to_roman_thousands(int(start_string[(len(start_string) - 4)]))

        conversion_string = thousands + hundreds + tens + ones

    return conversion_string


def main():
    # print("Test (450): '" + convert_to_roman_numeral(450) + "'")
    # print("Test (10000): '" + convert_to_roman_numeral(10000) + "'")
    # print("Test (1): '" + convert_to_roman_numeral(1) + "'")
    # print("Test (29): '" + convert_to_roman_numeral(29) + "'")
    # print("Test (2000): '" + convert_to_roman_numeral(2000) + "'")
    # print("Test (4500): '" + convert_to_roman_numeral(4500) + "'")
    # print("Test (86): '" + convert_to_roman_numeral(86) + "'")
    # print("Test (9999): '" + convert_to_roman_numeral(9999) + "'")
    # print("Test (5000): '" + convert_to_roman_numeral(5000) + "'")
    # print("Test (5050): '" + convert_to_roman_numeral(5050) + "'")
    # print("Test (499): '" + convert_to_roman_numeral(499) + "'")

    doctest.testmod()


if __name__ == "__main__":
    main()

"""Components of computational thinking  (decomposition, pattern matching, abstraction, algorithms) used in this script:
Decomposition was used to split out the code needed to convert a single digit.
convert_digit_to_roman_numeral makes use of algorithms.
Abstraction: via the creation of both functions: hiding complexity from the user, creating a "black box".
Data representation is seen in the breaking up of each digit in the decimal number to it's order of magnitude.
 """
