# based off https://github.com/simpeg-research/heagy-2018-AEM/blob/master/tests/test_notebooks.py

import os
import testipynb
import unittest

NBDIR = os.path.sep.join(
    os.path.abspath(__file__).split(os.path.sep)[:-2] + ['nb']
)

class TestNotebooks(unittest.TestCase):

    def test_notebooks(self):
        Test = testipynb.TestNotebooks(directory=NBDIR)
        self.assertTrue(Test.run_tests())

if __name__ == "__main__":
    unittest.main()
