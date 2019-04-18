#! /usr/bin/env python
#! -*- coding: utf-8 -*-

import logging
import unittest
import sys
import math

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    handlers=[
                        logging.StreamHandler(sys.stdout)
                    ])

logger = logging.getLogger(__name__)


class MathTest(unittest.TestCase):

    def test_num_eq(self):
        self.assertEqual(4.0, 2.0 * 2)
        self.assertEqual(4.05, 8.1 / 2)

    def test_isclose(self):
        self.assertTrue(math.isclose(1.995, 2.0, rel_tol=5e-3))
        self.assertTrue(math.isclose(2, 2.005, rel_tol=5e-3))


suite = unittest.TestLoader().loadTestsFromTestCase(MathTest)
unittest.TextTestRunner(verbosity=2).run(suite)
