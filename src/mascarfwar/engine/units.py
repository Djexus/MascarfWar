class Unit(object):

    '''
    Docstring missing...

    Usage:
    >>> unit = Unit(image)
    >>> unit.can_move(world, (1, 1))
    >>> unit.can_attack(world, other)
    >>> unit.kill()
    '''

    def __init__(self, image):

        self.image = image
        self.is_alive = True

    def can_move(self, world, position):

        raise NotImplementedError

    def can_attack(self, world, enemy):

        raise NotImplementedError

    def availaible_moves(self, world):

        return (self.can_move(world, x) for x in world.coords)

    def availaible_attacks(self, world):

        return (self.can_attack(world, x) for x in world.units)

    def kill(self):

        self.is_alive = False


class Ground(Unit):

    '''
    Docstring missing...

    Usage:
    >>> ground = Ground(image)
    '''

    def can_move(self, world, position):

        return False

    def can_attack(self, world, enemy):

        return False
