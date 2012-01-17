'''
Docstring missing...
'''


class Unit(object):

    '''
    Docstring missing...
    '''

    def __init__(self, image):

        self.image = image
        self.is_alive = True

    def can_move(self, world, position):

        raise NotImplementedError

    def can_attack(self, world, enemy):

        raise NotImplementedError

    def availaible_moves(self, world):

        return filter(lambda x: self.can_move(world, x), world.coords)

    def availaible_attacks(self, world):

        return filter(lambda x: self.can_attack(world, x),  world.units)

    def kill(self):

        self.is_alive = False


class Ground(Unit):

    '''
    Docstring missing...
    '''

    def can_move(self, world, position):

        return False

    def can_attack(self, world, enemy):

        return False
