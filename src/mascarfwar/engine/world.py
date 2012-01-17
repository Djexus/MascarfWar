'''
Docstring missing...
'''


class World(object):

    '''
    Docstring missing...
    '''

    def __init__(self, mapsize, cellsize):

        self.mapsize = mapsize
        self.cellsize = cellsize
        self.coords = [(x, y) for x in range(mapsize[0]) for y in range(mapsize[1])]
        self.tags = collections.defaultdict(set)

    def add_unit(self, unit, position, *tags):

        for tag in tags:
            self.tags[tag].add(unit)

    def remove_unit(self, unit):

        for tag in tags:
            self.tags[tag].discard(unit)

    def move_unit(self, unit, position):

        if (position in self.coords) and unit.can_move(self, position):
            pass
    
    def attack_unit(self, unit, enemy):

        if unit.can_attack(self, enemy):
            pass

    def cleanup(self):

        for unit in self.units:
            self.remove_unit(unit)

    def get(self, *tags):

        return reduce(set.intersection, (self.tags[x] for x in tags))
