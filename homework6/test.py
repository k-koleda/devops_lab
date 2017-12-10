"""Unit test for script"""
import unittest
import script


class TestScript(unittest.TestCase):
    """Unit test class"""
    def setUp(self):
        """Init"""

    def test_len_output(self):
        """Is there dict?"""
        self.assertTrue(script.output)

    def tearDown(self):
        """Finish"""


if __name__ == '__main__':
    unittest.main()
