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
        matrix = np.array(([1,1,0,1],[0,1,1,0],[0,0,1,1],[1,0,0,1]))
        self.assertEqual(main.rule_checker(matrix)[0], 5)
    
    def test_rule3_2(self):
        matrix = np.array(([1,1,0,1],[0,1,1,0],[0,0,1,1],[1,0,0,1]))
        self.assertEqual(main.rule_checker(matrix)[0], 6)

if __name__ == '__main__' :
    unittest.main(verbosity=0)