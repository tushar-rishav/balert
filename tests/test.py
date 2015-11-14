import sys
sys.path.append('../balert/')
from balert.Voice import Voice
from balert.Config import Config
from balert.BatteryStatus import Battery
from balert.Bsettings import Bpath, SetLevel
import unittest2
import logging
import sys
import os

if sys.version_info >= (3,):
    import pickle
else:
    import cPickle as pickle


class BalertTestCase(unittest2.TestCase):

    """
        Tests for `balert/main.py`.
    """

    def setUp(self):
        self.power_source = ("Mains", "UPS", "Battery")
        self.D_CONF = {
            "CHARGE": 20,
            "LANG": "english",
            "RATE": 150,
            "MSG": "",
            "VOL": 1.0,
        }

    def test_power_source(self):
        """
            Test Battery Status module
        """
        self.bat = Battery()
        for supply in os.listdir(Bpath.POWER_SUPPLY_PATH):
            supply_path = os.path.join(Bpath.POWER_SUPPLY_PATH, supply)
            _type = self.bat.power_source_type(supply_path)
            query = _type in self.power_source
            self.assertEqual(query, True)
            try:
                capacity = int(self.bat.state(supply_path))
                self.assertTrue(capacity <= 100 and capacity >= 0, True)
            except Exception as e:
                print e, "But no issues"

    def test_config(self):
        """
            Test Config module
        """
        self.cf = Config()
        self.D_CONF["CHARGE"] = 100
        self.cf.set_pickle(self.D_CONF)
        self.assertEqual(
            self.cf.load_pickle(), self.D_CONF)


if __name__ == "__main__":
    unittest2.main()
