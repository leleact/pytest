#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import logging
import requests
from lxml import etree, html

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    handlers=[
                        logging.StreamHandler(sys.stdout)
                    ])
logger = logging.getLogger(__name__)

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'


def main():
    url = "https://www.google.com"
    response = requests.get(url, headers={
        'User-Agent': user_agent
    }, proxies={
        'http': 'http://10.0.0.1:18080',
        'https': 'https://10.0.0.1:18080'
    })
    logger.debug("response text: %s", response.text)


if __name__ == '__main__':
    main()
