'''
Docstring missing...
'''


class Group(object):

    '''
    Docstring missing...
    '''

    def __init__(self, units=[]):
        
        self.units = set(units)

    def __contains__(self, item):

        return item in self.units

    def __iter__(self):

        return iter(self.units)

    def add(self, unit):

        self.units.add(unit)

    def remove(self, unit):
        
        return self.units.remove(unit)
    
    def cleanup(self):

        return [self.remove(x) for x in self.units if not x.is_alive]

    def get(self, **tags):
        
        return Group([x for x in self.units if all(x[k] == v for k, v in tags.items())])


class Field(Group):

    '''
    Docstring missing...
    '''

    def __init__(self, mapsize, cellsize):

        self.mapsize = mapsize
        self.cellsize = cellsize
        self.coords = [(x, y) for x in range(mapsize[0]) for y in range(mapsize[1])]
        super(Field, self).__init__()
