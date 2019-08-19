#! /usr/bin/env python
#! -*- coding: utf-8 -*-

import logging
import unittest
import sys
import os
import subprocess

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    handlers=[
                        logging.StreamHandler(sys.stdout)
                    ])

logger = logging.getLogger(__name__)

subprocess.call(['ls', '-l'])
