#! /usr/bin/env python
#! -*- coding: utf-8 -*-

import logging
import unittest
import sys
import math
from decimal import *

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    handlers=[
                        logging.StreamHandler(sys.stdout)
                    ])

logger = logging.getLogger(__name__)


class DecimalTest(unittest.TestCase):

    def test_compare(self):
        dc1 = {'c1': 1190.0, 'c2': Decimal('1185')}
        logger.debug("%s", dc1["c1"])
        logger.debug("%s", dc1["c2"])
        self.assertTrue(math.isclose(dc1["c1"], dc1["c2"], rel_tol=5e-3))
        self.assertFalse(abs(Decimal(dc1["c1"]) - Decimal(dc1["c2"])) <= 0.005)
        dc2 = {'c1': 1190.004, 'c2': Decimal('1190.005')}
        logger.debug("%s", dc2["c1"])
        logger.debug("%s", dc2["c2"])
        self.assertTrue(math.isclose(dc2["c1"], dc2["c2"], rel_tol=5e-3))
        self.assertTrue(abs(Decimal(dc2["c1"]) - Decimal(dc2["c2"])) <= 0.005)


suite = unittest.TestLoader().loadTestsFromTestCase(DecimalTest)
unittest.TextTestRunner(verbosity=2).run(suite)
