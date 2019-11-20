def dijkstra(lst: list):
    """
    Sort a list of strings.

    :param lst: list of strings ['red', 'white', 'blue'] in any order, repeated any amount of times
    :precondition: lst is non-empty
    :precondition: lst can contain only ['red', 'white', 'blue']
    :postcondition: sorts list such that every 'red' appears first, then every 'white', then every 'blue'

    >>>dijkstra(['red', 'white', 'blue'])
    ['red', 'white', 'blue']
    >>>dijkstra(['blue', 'red', 'white', 'blue'])
    ['red', 'white', 'blue', 'blue]
    >>>dijkstra(['white', 'blue', 'blue', 'red', 'white', 'red', 'white'])
    ['red', 'red', 'white', 'white', 'white', 'blue', 'blue']
    """

    lst.sort()

    while lst[0] != 'red':
        lst.append(lst.pop(0))
