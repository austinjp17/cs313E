import unittest

from Josephus import CircularList

ELEMENTS = 10

class circular_linked_list_unit_tests(unittest.TestCase):
    
    ELEMENTS = 10
    EXPECTED_INIT_LIST = "1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 1 -> 2 -> 3 -> ..."

    def test_circular_list(self):

        # Test 1: Creation
        circle = CircularList()
        self.assertEqual(str(circle), "None")
    
        # Test 2: Insert
        for i in range(1, ELEMENTS+1):
            circle.insert(i)
        self.assertEqual(str(circle), EXPECTED_INIT_LIST)

    

if __name__ == "__main__":
    unittest.main()