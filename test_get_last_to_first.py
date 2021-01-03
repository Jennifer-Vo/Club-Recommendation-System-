"""A3. Test cases for function club_functions.get_last_to_first.
"""

import unittest
import club_functions


class TestGetLastToFirst(unittest.TestCase):
    """Test cases for function club_functions.get_last_to_first.
    """

    def test_00_empty(self):
        param = {}
        actual = club_functions.get_last_to_first(param)
        expected = {}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_01_one_person_one_friend_same_last(self):
        param = {'Clare Dunphy': ['Phil Dunphy']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare', 'Phil']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)        
        
    def test_02_one_person_many_friends_same_last(self):
        param = {'Claire Dunphy': ['Jennifer Dunphy', 'Sophia Dunphy', 
                                   'Gab Dunphy']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Claire', 'Gab', 'Jennifer', 'Sophia']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)        
        
    def test_03_one_person_many_friends_different_last(self):
        param = {'Claire Dunphy': ['Phil Vo', 'Sophia Huang', 'Merve Younessi']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Claire'], 'Vo': ['Phil'], 'Huang': ['Sophia'],
                    'Younessi': ['Merve']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
    def test_04_many_people_many_friends_same_last(self):
        param = {'Claire Dunphy': ['Sophia Dunphy', 'Hugo Dunphy', 
                                   'Merve Dunphy'], 
                 'Gab Dunphy': ['Thomas Dunphy', 'Axel Dunphy']} 
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Axel', 'Claire', 'Gab', 'Hugo','Merve',
                               'Sophia', 'Thomas']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
    def test_05_many_people_many_friends_different_last(self):
        param = {'Claire Dunphy': ['Phil Dunphy', 'Sophia Huang', 
                                   'Merve Dunphy'], 'Claire Trottier': 
                 ['Dominique Walker', 'Olga Tsyruk']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Claire', 'Merve', 'Phil'], 'Huang': ['Sophia'], 
                    'Walker': ['Dominique'], 'Trottier': ['Claire'], 
                    'Tsyruk':['Olga']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)        
        
    def test_06_many_people_some_mutual_friends_different_last(self):
        param = {'Claire Dunphy': ['Phil Dunphy', 'Sophia Huang', 
                                   'Merve Dunphy'], 'Claire Trottier': 
                 ['Dominique Walker', 'Sophia Huang']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Claire', 'Merve', 'Phil'], 'Huang': ['Sophia'], 
                    'Walker': ['Dominique'], 'Trottier': ['Claire']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg) 
         
       
        
if __name__ == '__main__':
    unittest.main(exit=False)
