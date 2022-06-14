import numpy as np
import main
import unittest

class TestRuleChecking(unittest.TestCase):
    def test_rule1_1(self):
        matrix = np.array(([0,0,1,0],[0,1,0,1],[1,1,0,0],[0,0,1,0]))
        self.assertEqual(main.rule_checker(matrix)[0], 1)
    
    def test_rule1_2(self):
        matrix = np.array(([1,1,0,1],[0,0,1,0],[0,0,1,1],[1,1,0,0]))
        self.assertEqual(main.rule_checker(matrix)[0], 2)

    def test_rule2_1(self):
        matrix = np.array(([0,0,0,1],[0,1,0,1],[1,1,0,0],[0,0,1,0]))
        self.assertEqual(main.rule_checker(matrix)[0], 3)
    
    def test_rule2_2(self):
        matrix = np.array(([1,0,1,1],[0,0,1,0],[0,0,1,1],[1,1,0,0]))
        self.assertEqual(main.rule_checker(matrix)[0], 4)

    def test_rule3_1(self):
        matrix = np.array(([1,1,0,1,0,0],[1,0,0,1,1,0],[0,1,1,0,1,1],[1,0,1,1,0,0],[0,1,0,1,0,1],[0,0,1,0,1,1]))
        self.assertEqual(main.rule_checker(matrix)[0], 5)
    
    def test_rule3_2(self):
        matrix = np.array(([5641,6854,1,1,6784,5411],[9851,1515,8545,1,0,0],[3248,5145,2187,0,67874,0],[2414,8753,4879,1,9548,2166],[6854,0,6874,1,1,6156],[7797,0,4187,0,8756,45478]))
        self.assertEqual(main.rule_checker(matrix)[0], 6)

if __name__ == '__main__' :
    unittest.main(verbosity=0)