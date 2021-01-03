"""A3. Test cases for function club_functions.get_average_club_count.
"""

import unittest
import club_functions


class TestGetAverageClubCount(unittest.TestCase):
    """Test cases for function club_functions.get_average_club_count.
    """

    def test_00_empty(self):
        param = {}
        actual = club_functions.get_average_club_count(param)
        expected = 0.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg=msg)

    def test_01_one_person_one_club(self):
        param = {'Claire Dunphy': ['Parent Teacher Association']}
        actual = club_functions.get_average_club_count(param) 
        expected = 1.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg=msg)
    
    def test_02_one_person_many_clubs(self):
        param = {'Claire Dunphy': ['BJJ', 'ABC', 'Flying', 'Eating']}
        actual = club_functions.get_average_club_count(param)
        expected = 4.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg=msg)      
        
    def test_03_many_people_one_club(self):
        param = {'Claire Dunphy': ['BJJ'], 'Jennifer Vo': ['Eating'], 
                 'Sophia Huang': ['BJJ']}
        actual = club_functions.get_average_club_count(param)
        expected = 1.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg=msg)      
        
    def test_04_many_people_many_clubs(self):
        param = {'Claire Dunphy': ['BJJ', 'ABC'], 'Jennifer Vo': ['BJJ'], 
                 'Sophia Huang': ['Flying', 'Cooking', 'Cleaning', 'Sleep']}
        actual = club_functions.get_average_club_count(param)
        expected = 7/3
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg=msg)        
    
        
    
if __name__ == '__main__':
    unittest.main(exit=False)
