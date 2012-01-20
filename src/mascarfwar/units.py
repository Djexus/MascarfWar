'''
Docstring missing...
'''


GROUND_NORMAL = 'normal'
GROUND_FLYZONE = 'fly zone'
GROUND_NOFLYZONE = 'no fly zone'

UNIT_INFANTRY = 'infantry'
UNIT_SNIPER = 'sniper'
UNIT_TANK_CANNON = 'tank with cannon'
UNIT_TANK_MACHINE_GUN = 'tank with machine gun'
UNIT_ANTI_TANK = 'anti tank'
UNIT_HALFTRACK = 'halftrack'
UNIT_BOMBER = 'bomber'
UNIT_AIRCRAFT = 'aircraft'
UNIT_ANTI_AIRCRAFT = 'anti aircraft'


class Unit(object):

    '''
    Docstring missing...
    '''

    def __init__(self, images, **tags):

        self.images = dict(images)
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

        return filter(lambda x: self.can_move(field, x), field.coords)

    def availaible_attacks(self, field):

        return filter(lambda x: self.can_attack(field, x),  field.units)

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

    def kill(self):

        pass


class Infantry(Unit):

    '''
    Docstring missing...
    '''

    def __init__(self, images, **tags):

        super(Infantry, self).__init__(images, dict(tags, type=UNIT_INFANTRY))

    def can_move(self, field, position):

        return (position in neighbours(self['position'])) and field.get(position=position)[0]['type'] != GROUND_FLYZONE

    def can_attack(self, field, enemy):

        pass


class Sniper(Unit):

    '''
    Docstring missing...
    '''

    def __init__(self, images, **tags):

        super(Sniper, self).__init__(images, dict(tags, type=UNIT_SNIPER))

    def can_move(self, field, position):

        pass

    def can_attack(self, field, enemy):

        pass


class TankCannon(Unit):

    '''
    Docstring missing...
    '''

    def __init__(self, images, **tags):

        super(TankCannon, self).__init__(images, dict(tags, type=UNIT_TANK_CANNON))

    def can_move(self, field, position):

        pass

    def can_attack(self, field, enemy):

        pass


class TankMachineGun(Unit):

    '''
    Docstring missing...
    '''

    def __init__(self, images, **tags):

        super(TankMachineGun, self).__init__(images, dict(tags, type=UNIT_TANK_MACHINE_GUN))

    def can_move(self, field, position):

        pass

    def can_attack(self, field, enemy):

        pass


class AntiTank(Unit):

    '''
    Docstring missing...
    '''

    def __init__(self, images, **tags):

        super(AntiTank, self).__init__(images, dict(tags, type=UNIT_ANTI_TANK))

    def can_move(self, field, position):

        pass

    def can_attack(self, field, enemy):

        pass


class Halftrack(Unit):

    '''
    Docstring missing...
    '''

    def __init__(self, images, **tags):

        super(Halftrack, self).__init__(images, dict(tags, type=UNIT_HALFTRACK))

    def can_move(self, field, position):

        pass

    def can_attack(self, field, enemy):

        pass


class Aircraft(Unit):

    '''
    Docstring missing...
    '''

    def __init__(self, images, **tags):

        super(Aircraft, self).__init__(images, dict(tags, type=UNIT_AIRCRAFT))

    def can_move(self, field, position):

        return (self['position'][0] == position[0]) and (field.get(position=position)[0]['type'] == GROUND_FLYZONE)

    def can_attack(self, field, enemy):

        pass


class AntiAircraft(Unit):

    '''
    Docstring missing...
    '''

    def __init__(self, images, **tags):

        super(AntiAircraft, self).__init__(images, dict(tags, type=UNIT_ANTI_AIRCRAFT))

    def can_move(self, field, position):

        pass

    def can_attack(self, field, position):

        pass
