'''
Docstring missing...
'''


class Unit(object):

    '''
    Docstring missing...
    '''

    def __init__(self, image, **tags):

        self.image = image
        self.is_alive = True
        self.tags = tags

    def __getitem__(self, item):

        return self.tags.get(item, None)

    def __setitem__(self, item, value):

        self.tags[item] = value

    def __delitem__(self, item):

        self.tags.pop(item)

    def can_move(self, field, position):

        raise NotImplementedError

    def can_attack(self, field, enemy):

        raise NotImplementedError

    def availaible_moves(self, field):

        return filter(lambda x: self.can_move(world, x), world.coords)

    def availaible_attacks(self, field):

        return filter(lambda x: self.can_attack(world, x),  world.units)

    def kill(self):

        self.is_alive = False


class Ground(Unit):

    '''
    Docstring missing...
    '''

    def can_move(self, field, position):

        return False

    def can_attack(self, field, enemy):

        return False
