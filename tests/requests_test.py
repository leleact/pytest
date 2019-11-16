#! /usr/bin/env python
#! -*- coding: utf-8 -*-

import logging
import unittest
import sys
import requests

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    handlers=[
                        logging.StreamHandler(sys.stdout)
                    ])

logger = logging.getLogger(__name__)


class SessionTest(unittest.TestCase):
    def test_session(self):
        s = requests.Session()
        r = s.get('https://httpbin.org/cookies')
        logger.debug('text: [%s], encoding: [%s], headers: [%s]', r.text, r.encoding, r.headers)


suite = unittest.TestLoader().loadTestsFromTestCase(SessionTest)
unittest.TextTestRunner(verbosity=2).run(suite)
