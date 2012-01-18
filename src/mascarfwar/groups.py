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


class Field(Group):

    '''
    Docstring missing...
    '''

    def __init__(self, mapsize, cellsize):

        self.mapsize = mapsize
        self.cellsize = cellsize
        self.coords = [(x, y) for x in range(mapsize[0]) for y in range(mapsize[1])]
        self.field = collections.defaultdict(list)
        super(Field, self).__init__()

    def add(self, unit, position):

        self.field[position].append(unit)
        super(Field, self).add(unit)

    def remove(self, unit):

        self.field[position].pop(unit)
        super(Field, self).remove(unit)

    def move_unit(self, unit, position):

        if (position in self.coords) and unit.can_move(self, position):
            pass

    def attack_unit(self, unit, enemy):

        if (enemy in self.units) and unit.can_attack(self, enemy):
            pass
