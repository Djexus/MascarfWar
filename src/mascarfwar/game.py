'''
Docstring missing...
'''


import units
import groups
import utilities


class Unit(units.Unit):

    '''
    Docstring missing...
    '''

    def can_move(self, field, position):

        pass
    
    def can_attack(self, field, enemy):

        pass


class Battle(object):

    '''
    Docstring missing...
    '''

    def __init__(self):

        self.world = groups.Field((11, 12), (10, 10))

    def update(events):

        pass

