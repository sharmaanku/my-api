import unittest
from app import add

class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)  # Test case should pass
        self.assertEqual(add(-1, 1), 0)  # Another test case

if __name__ == '__main__':
    unittest.main()

