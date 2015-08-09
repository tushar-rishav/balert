import os
from Bsettings import bpath,SetLevel

class battery(bpath):
	"""
		Module to fetch battery status
	"""
	sl = None
	def __init__(self):
		if not os.access(bpath.POWER_SUPPLY_PATH, os.R_OK):
			raise RuntimeError("Unable to read {path}.".format(path = bpath.POWER_SUPPLY_PATH))
		else:
			self.sl = SetLevel()
			print "All ok!"
	def is_ac_online(self,supply_path):
		with open(os.path.join(supply_path, 'online'), 'r') as online_file:
			return online_file.readline().strip() == '1'
	def power_source_type(self,supply_path):
		with open(os.path.join(supply_path, 'type'), 'r') as type_file:
			type = type_file.readline().strip()
			if type == 'Mains':
				return "Mains"
			elif type == 'UPS':
				return "UPS"
			elif type == 'Battery':
				return "Battery"
			else:
				raise RuntimeError("Type of {path} ({type}) is not supported".format(path=supply_path, type=type))
	def is_battery_present(self,supply_path):
		with open(os.path.join(supply_path, 'present'), 'r') as present_file:
			return present_file.readline().strip() == '1'

	def is_battery_discharging(self,supply_path):
		with open(os.path.join(supply_path, 'status'), 'r') as status_file:
			return status_file.readline().strip() == 'Discharging'
	
	def get_battery_state(self,supply_path):
		with open(os.path.join(supply_path, 'capacity'), 'r') as capacity_file:
			return capacity_file.readline().split()[0]

	def get_low_battery_warning_level(self):
		capacity=None
		for supply in os.listdir(bpath.POWER_SUPPLY_PATH):
			supply_path = os.path.join(bpath.POWER_SUPPLY_PATH, supply)
			try:
				type = self.power_source_type(supply_path)
				if type == "Mains":
					if self.is_ac_online(supply_path):
						pass
				elif type == "Battery":
					if self.is_battery_present(supply_path) and self.is_battery_discharging(supply_path):
						capacity = self.get_battery_state(supply_path)
						
				else:
					pass
			except Exception as e:
				print e

		try:
			if int(capacity) <= self.sl.CHARGE:
				return (1,capacity)
			else:
				return (0,None)
		except ZeroDivisionError as e:
			print e
