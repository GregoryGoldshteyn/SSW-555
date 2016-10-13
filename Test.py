import unittest
import Main

class TestSimpleProgram(unittest.TestCase):
	def test_orgCode(self):
		#Testing it works in general
		self.assertEqual(True, Main.checkValidTag("2 DATE 23 AUG 1940", Main.levelTags))
		self.assertEqual(True, Main.checkValidTag("2 DATE AUG 1940", Main.levelTags))
		self.assertEqual(True, Main.checkValidTag("2 DATE 1940", Main.levelTags))
		self.assertEqual(False, Main.checkValidTag("2 DATE", Main.levelTags))
		
if __name__ == '__main__':
	unittest.main()