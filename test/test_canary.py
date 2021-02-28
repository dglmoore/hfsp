import unittest
import hfsp


class TestCanary(unittest.TestCase):
    def test_canary(self):
        self.assertEquals('HFSP', hfsp.hfsp())
