import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    # Add your test methods for a1.stock_price_summary here.
    def test_initial_example(self):
    	'''Test the initial example with a random sample of gains and losses'''
    	actual = a1.stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
    	expected = (0.14, -0.17)
    	self.assertEqual(actual, expected)

    def test_zero_case(self):
    	'''Test an array of zeroes in the array and whether the result tuple is displaying correctly'''
    	actual = a1.stock_price_summary([0, 0, 0])
    	expected = (0, 0)
    	self.assertEqual(actual, expected)

    def test_only_gains(self):
    	'''Test a list of only gains and whether the result tuple is displaying correctly'''
    	actual = a1.stock_price_summary([5, 4, 3, 2, 1])
    	expected = (15, 0)
    	self.assertEqual(actual, expected)

    def test_only_losses(self):
    	'''Test a list of only losses and whether the result tuple is displaying correctly'''
    	actual = a1.stock_price_summary([-5, -4, -3, -2, -1])
    	expected = (0, -15)
    	self.assertEqual(actual, expected)

    def test_empty_list(self):
    	'''Test an empty list and whether the result tuple is displaying correctly'''
    	actual = a1.stock_price_summary([])
    	expected = (0, 0)
    	self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(exit=False)
