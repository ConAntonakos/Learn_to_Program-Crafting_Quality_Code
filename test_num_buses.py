import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    # Add your test methods for a1.num_buses here.
    def test_num_buses(self):
    	actual = a1.num_buses(75)
    	expected = 2
    	self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(exit=False)
