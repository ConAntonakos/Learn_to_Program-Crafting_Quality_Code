import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    # Add your test methods for a1.swap_k here.
    def test_swap_k(self):
    	actual = a1.swap_k([1, 2, 3, 4, 5, 6], 2)
    	expected = [5, 6, 3, 4, 1, 2]
    	self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(exit=False)
