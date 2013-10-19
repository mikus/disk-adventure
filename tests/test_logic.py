import unittest

from adventure import dojo


class TestLogic(unittest.TestCase):

	def test_0_hops_between_same_paths(self):
		assert dojo.distance('/usr/bin/python', '/usr/bin/python') == 0

	def test_1_hop_between_realtive_paths(self):
		assert dojo.distance('/usr/bin/python', '/usr/bin') == 1
		assert dojo.distance('/usr/bin', '/usr/bin/python') == 1
        
   	def test_hops_between_unrelated_paths(self):
		assert dojo.distance('/usr/bin/python', '/home/foo/bar') == 6
		assert dojo.distance('/home/foo', '/usr/bin/python') == 5
        

if __name__ == '__main__':
	unittest.main()