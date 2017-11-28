import unittest
import maths

class TestMaths(unittest.TestCase):
	def test_sum(self):
		self.assertEqual(maths.sum(10, 5), 15)
		
if __name__ == "__main__":
	unittest.main()