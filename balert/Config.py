import os
import logging
import sys
import getpass
if sys.version_info >= (3,):
    import pickle
else:
    import cPickle as pickle

logging.getLogger().name = "Balert# "


class Config:
    D_CONF = {
        "CHARGE": 20,
        "LANG": "english",
        "RATE": 150,
        "MSG": "",
        "VOL": 1.0,
    }
    CUR_DIR = "/home/"+getpass.getuser()
    FILE_PATH = os.path.join(CUR_DIR, ".balertrc")

    def __init__(self):
        pass

    def set_pickle(self, obj):
        try:
            f = open(Config.FILE_PATH, 'wb')
            os.chmod(Config.FILE_PATH, 0o777)
            pickle.dump(obj, f)
            f.close()
        except Exception as e:
            logging.debug(str(e))

    def load_pickle(self):
        if os.path.exists(Config.FILE_PATH):
            os.chmod(Config.FILE_PATH, 0o777)
            f = open(Config.FILE_PATH, 'r')
            D_C = pickle.load(f)    # USE THIS NOW
            f.close()
            return D_C

        else:
            self.set_pickle(Config.D_CONF)
            return Config.D_CONF
