#! /usr/bin/env python
#! -*- coding: utf-8 -*-

import logging
import unittest
import sys

fh = logging.FileHandler('/tmp/app.log')
fh.setLevel(logging.DEBUG)

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    handlers=[
                        fh,
                        logging.StreamHandler(sys.stdout)
                    ])

logger = logging.getLogger(__name__)


class LoggingTest(unittest.TestCase):

    def test_debug_log(self):
        logger.debug("xxx")
        self.assertEqual(4, 2+2)


suite = unittest.TestLoader().loadTestsFromTestCase(LoggingTest)
unittest.TextTestRunner(verbosity=2).run(suite)
