class bpath:
    POWER_SUPPLY_PATH = '/sys/class/power_supply'
    def __init__(self):
        pass

class SetLevel:
    TIME = 10
    CHARGE = 20
    def __init__(self):
        pass
    def time(self,time):
        self.TIME = time
    def charge(self,charge):
        self.CHARGE = charge