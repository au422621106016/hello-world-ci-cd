
import unittest
from app import hello_world

class Testapp(unittest,Testcase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), "Hello, World!")

if _name_== '_main_':
    unittest.main()
            