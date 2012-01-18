'''
Docstring missing...
'''


class Group(object):

    '''
    Docstring missing...
    '''

    def __init__(self, units=[]):

        self.units = set(units)

    def add(self, unit):

        self.units.add(unit)

    def remove(self, unit):

        return self.units.remove(unit)

    def cleanup(self):

        return [self.remove(x) for x in self.units if not x.is_alive]

    def get(self, **tags):

        return [x for x in self.units if all(x[k] == v for k, v in tags.items())] 


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
