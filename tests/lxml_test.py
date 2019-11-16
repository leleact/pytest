#! /usr/bin/env python
#! -*- coding: utf-8 -*-

import logging
import unittest
import sys
import requests
from lxml import html, etree
from io import StringIO

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    handlers=[
                        logging.StreamHandler(sys.stdout)
                    ])

logger = logging.getLogger(__name__)

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'


class HTMLTest(unittest.TestCase):
    def test_html_parse(self):
        url = 'https://www.ithome.com/'
        response = requests.get(url, headers={
            'User-Agent': user_agent
        })
        response.encoding = 'utf-8'
        tree = html.fromstring(response.text)
        s = tree.xpath(
            '//div[@class="lst lst-1 new-list"]//li/span[2]/a/text()')
        logger.debug('%s', s)
        self.assertIsNotNone(s)

    def test_etree_html_parse(self):
        url = 'https://www.ithome.com/'
        response = requests.get(url, headers={
            'User-Agent': user_agent
        })
        response.encoding = 'utf-8'
        tree = etree.parse(StringIO(response.text), etree.HTMLParser())
        s = tree.xpath(
            '//div[@class="lst lst-1 new-list"]//li/span[2]/a/text()')
        logger.debug('%s', s)
        self.assertIsNotNone(s)


suite = unittest.TestLoader().loadTestsFromTestCase(HTMLTest)
unittest.TextTestRunner(verbosity=2).run(suite)
