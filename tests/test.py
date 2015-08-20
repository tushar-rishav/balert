import subprocess,unittest2

class BalertTestCase(unittest2.TestCase):
    """Tests for `balert/main.py`."""
    
    def run_balert(self):
    	balert_run = subprocess.Popen("balert", shell=True, stdout=subprocess.PIPE).stdout.read()
    	if "Ok" in balert_run:
        	return True
        else:
        	return False

    def test_balert(self):
		self.assertTrue(self.run_balert())

if __name__ == "__main__":
    unittest2.main()
