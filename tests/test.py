import subprocess,unittest

class BalertTestCase(unittest.TestCase):
    """Tests for `balert/main.py`."""
    
    def run_balert(self):
    	balert_run = subprocess.Popen("balert", shell=True, stdout=subprocess.PIPE).stdout.read()
    	cron_check = subprocess.Popen("crontab -l", shell=True, stdout=subprocess.PIPE).stdout.read()
        print cron_check
        print "balert" in cron_check
        if "balert" in cron_check:
        	return True
        else:
        	return False

    def test_balert(self):
		self.assertTrue(self.run_balert())

if __name__ == "__main__":
    unittest.main()
