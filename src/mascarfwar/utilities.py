'''
Docstring missing...
'''


DIRECTIONS = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))


def add_point(x, y):

    '''
    Docstring missing...

    Usage:
    >>> add_point((2, 1), (-1, 0))
    (1, 1)
    '''

    return (x[0] + y[0], x[1] + y[1])


def neighbours(pos):

    '''
    Docstring missing...

    Usage:
    >>> neighbours((1, 1))
    [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)]
    '''

    return [add_point(pos, x) for x in DIRECTIONS]
