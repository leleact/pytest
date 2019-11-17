#!/usr/bin/env python

import logging
import unittest
import sys

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    handlers=[
                        logging.StreamHandler(sys.stdout)
                    ])

logger = logging.getLogger(__name__)


class A:
    pass


class TypeTest(unittest.TestCase):
    def test_type(self):
        l = []
        d = {}
        a = A()
        logger.debug("type of l is %s, %s", type(l), isinstance(l, list))
        logger.debug("type of d is %s, %s", type(d), isinstance(d, dict))
        logger.debug("type of a is %s, %s", type(a), isinstance(a, A))
        self.assertEqual(4, 2+2)


suite = unittest.TestLoader().loadTestsFromTestCase(TypeTest)
unittest.TextTestRunner(verbosity=2).run(suite)
