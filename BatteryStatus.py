import os
from Bpath import bpath

class battery(bpath):
	"""
		Module to fetch battery status
	"""
	def __init__(self):
		if not os.access(bpath.POWER_SUPPLY_PATH, os.R_OK):
			raise RuntimeError("Unable to read {path}.".format(path = bpath.POWER_SUPPLY_PATH))
		else:
			print "All ok!"