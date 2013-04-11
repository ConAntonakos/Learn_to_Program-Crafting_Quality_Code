import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    # Add your test methods for a1.swap_k here.
    def test_initial_example_swap_2(self):
    	'''Initial example to test swapping 2 items'''
    	actual = a1.swap_k([1, 2, 3, 4, 5, 6], 2)
    	expected = [5, 6, 3, 4, 1, 2]
    	self.assertEqual(actual, expected)

    def test_swap_0(self):
    	'''Test swapping 0 item(s) in the input list'''
    	actual = a1.swap_k([1, 2, 3, 4, 5, 6], 6)
    	expected = [1, 2, 3, 4, 5, 6]
    	self.assertEqual(actual, expected)

    def test_swap_1(self):
    	'''Test swapping 1 item in the input list'''
    	actual = a1.swap_k([1, 2, 3, 4, 5, 6], 1)
    	expected = [6, 2, 3, 4, 5, 1]
    	self.assertEqual(actual, expected)

    def test_swap_3(self):
    	'''Test swapping 3 items in the input list'''
    	actual = a1.swap_k([1, 2, 3, 4, 5, 6], 3)
    	expected = [4, 5, 6, 1, 2, 3]
    	self.assertEqual(actual, expected)

    def test_swap_4(self):
    	'''Test swapping 4 items in the input list'''
    	actual = a1.swap_k([1, 2, 3, 4, 5, 6], 4)
    	expected = [5, 4, 6, 2, 3, 1]
    	self.assertEqual(actual, expected)

    def test_swap_5(self):
    	'''Test swapping 5 items in the input list'''
    	actual = a1.swap_k([1, 2, 3, 4, 5, 6], 5)
    	expected = [5, 4, 6, 2, 1, 3]
    	self.assertEqual(actual, expected)

    def test_swap_6(self):
    	'''Test swapping 6 items in the input list'''
    	actual = a1.swap_k([1, 2, 3, 4, 5, 6], 6)
    	expected = [1, 2, 3, 4, 5, 6]
    	self.assertEqual(actual, expected)

    def test_empty_list(self):
    	actual = a1.swap_k([], 1)
    	expected = "Nothing to swap!"
    	self.assertEqual(actual, expected)










if __name__ == '__main__':
    unittest.main(exit=False)
