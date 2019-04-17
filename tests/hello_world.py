#! /usr/bin/env python
#! -*- coding: utf-8 -*-

import logging
import unittest
import sys

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    handlers=[
                        logging.StreamHandler(sys.stdout)
                    ])

logger = logging.getLogger(__name__)


class HelloWorldTest(unittest.TestCase):

    def test_num_eq(self):
        self.assertEqual(4, 2+2)


suite = unittest.TestLoader().loadTestsFromTestCase(HelloWorldTest)
unittest.TextTestRunner(verbosity=2).run(suite)
