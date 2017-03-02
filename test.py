import unittest

import my_functions

class TestMyFunc(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def is_equal(self):
        self.assertEqual( my_functions.is_equal(2), 4)

if __name__ == '__main__':
    unittest.main()