# SPDX-FileCopyrightText: 2024-present tony <anthony.faizandier@etu.uca.fr>
#
# SPDX-License-Identifier: MIT

import unittest
from src.my_arithmetic_faizandier.fonction import gcd

class TestGCD(unittest.TestCase):
    def test_gcd(self):
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(101, 10), 1)
        self.assertEqual(gcd(0, 10), 10)
        self.assertEqual(gcd(10, 0), 10)
        
if __name__ == "__main__":
    unittest.main()


