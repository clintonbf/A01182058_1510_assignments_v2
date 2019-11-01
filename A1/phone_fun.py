import doctest


def translate_digit(digit):
    """
    Converts alphabetic digit to its telephonic equivalent.

    :param digit: string
    :precondition: single digit string
    :postcondition: the numeric equivalent (on a telephone) if argument is a letter, the same value if a number
    :return: int

    >>> translate_digit("1")
    '1'
    >>> translate_digit("D")
    3
    """

    return_value = None

    if digit in "0123456789":
        return_value = digit
    elif digit.lower() in "abcdefghijklmnopqrstuvwxyz":
        upper_digit = digit.upper()

        if upper_digit in "ABC":
            return_value = 2
        elif upper_digit in "DEF":
            return_value = 3
        elif upper_digit in "GHI":
            return_value = 4
        elif upper_digit in "JKL":
            return_value = 5
        elif upper_digit in "MNO":
            return_value = 6
        elif upper_digit in "PQRS":
            return_value = 7
        elif upper_digit in "TUV":
            return_value = 8
        elif upper_digit in "WXYZ":
            return_value = 9

    return return_value


def number_translator():
    """
    Translate the alphabetic components of a phone number into its numeric (on a telephone) equivalent.

    :return: string
    """

    ph_number = input("Enter a valid phone number: ")

    area_code = str(translate_digit(ph_number[0]) + translate_digit(ph_number[1]) + (translate_digit(ph_number[2])))
    exchange = str(translate_digit(ph_number[4])) + translate_digit(ph_number[5]) + translate_digit(ph_number[6])
    # This line had to be broken up to prevent PEP errors
    final_part = str(translate_digit(ph_number[8]) + translate_digit(ph_number[9]))
    final_part = final_part + str(translate_digit(ph_number[10]) + translate_digit(ph_number[11]))

    print("Translated #: " + area_code + "-" + exchange + "-" + final_part)


def main():
    # number_translator()
    doctest.testmod()


if __name__ == "__main__":
    main()

"""
Components of computational thinking  (decomposition, pattern matching, abstraction, algorithms) used in this script:
translate_digit() employs decomposition, pattern matching, abstraction,
    and algorithmic thinking to process the arguments.
"""
