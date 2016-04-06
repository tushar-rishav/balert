from Bsettings import Bpath
from Bsettings import SetLevel
from Config import Config
import logging
import os


class Battery(Bpath, Config):
    """
        Module to fetch battery status
    """

    def __init__(self):
        if not os.access(Bpath.POWER_SUPPLY_PATH, os.R_OK):
            raise RuntimeError("Unable to read {path}.\
                ".format(path=Bpath.POWER_SUPPLY_PATH))
        else:
            logging.debug("All ok!")
            self.charging = False

    def ac(self, supply_path):
        with open(os.path.join(supply_path, 'online'), 'r') as online_file:
            return online_file.readline().strip() == '1'

    def power_source_type(self, supply_path):
        with open(os.path.join(supply_path, 'type'), 'r') as type_file:
            _type = type_file.readline().strip()
            if _type == 'Mains':
                return "Mains"
            elif _type == 'UPS':
                return "UPS"
            elif _type == 'Battery':
                return "Battery"
            else:
                raise RuntimeError("Type of {path} ({type}) is not supported\
                    ".format(path=supply_path, type=type))

    def battery_present(self, supply_path):
        with open(os.path.join(supply_path, 'present'), 'r') as present_file:
            return present_file.readline().strip() == '1'

    def discharging(self, supply_path):
        with open(os.path.join(supply_path, 'status'), 'r') as status_file:
            return status_file.readline().strip() == 'Discharging'

    def state(self, supply_path):
        with open(os.path.join(supply_path, 'capacity'), 'r') as capacity_file:
            return capacity_file.readline().split()[0]

    def get_low_battery_warning_level(self):
        capacity = None
        for supply in os.listdir(Bpath.POWER_SUPPLY_PATH):
            supply_path = os.path.join(Bpath.POWER_SUPPLY_PATH, supply)
            try:
                _type = self.power_source_type(supply_path)
                if _type == "Mains":
                    if self.ac(supply_path):
                        pass
                elif _type == "Battery":
                    if self.battery_present(supply_path) and \
                       self.discharging(supply_path):
                        capacity = int(self.state(supply_path))
                    else:
                        self.charging = True

            except Exception as e:
                print(e)

        try:
            logging.getLogger().setLevel(logging.DEBUG)
            conf_charge = self.load_pickle()["CHARGE"]
            if not self.charging:
                logging.info("Current charge is %d, Level set is %d",
                              capacity, conf_charge)
                if capacity <= conf_charge:
                    return (1, capacity)
                else:
                    return (0, capacity)
            else:
                return (0, 0)
        except ZeroDivisionError as e:
            print(e)
