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


xml_str = '''
<?xml version="1.0" encoding="UTF-8"?>

<bookstore>

<book category="cooking">
  <title lang="en">Everyday Italian</title>
  <author>Giada De Laurentiis</author>
  <year>2005</year>
  <price>30.00</price>
</book>

<book category="children">
  <title lang="en">Harry Potter</title>
  <author>J K. Rowling</author>
  <year>2005</year>
  <price>29.99</price>
</book>

<book category="web">
  <title lang="en">XQuery Kick Start</title>
  <author>James McGovern</author>
  <author>Per Bothner</author>
  <author>Kurt Cagle</author>
  <author>James Linn</author>
  <author>Vaidyanathan Nagarajan</author>
  <year>2003</year>
  <price>49.99</price>
</book>

<book category="web">
  <title lang="en">Learning XML</title>
  <author>Erik T. Ray</author>
  <year>2003</year>
  <price>39.95</price>
</book>

</bookstore>
'''


def get_tree():
    url = 'https://www.ithome.com/'
    response = requests.get(url, headers={
        'User-Agent': user_agent
    })
    response.encoding = 'utf-8'
    # etree.parse 传入的类型是 stream?? parser 需要 HTMLParser 否则<!DOCTYPE html>不能解析
    return etree.parse(StringIO(response.text), etree.HTMLParser())


def get_xml_tree():
    return etree.XML(xml_str, parser=etree.XMLParser(ns_clean=True, recover=True, encoding='utf-8'))


def show_list(name, l):
    logger.debug("name = %s, num = %s", name, len(l))
    for i in l:
        logger.debug('name=%s, d=%s', name, etree.tostring(i, encoding='utf-8').decode('utf-8'))


class XPathTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(XPathTest, self).__init__(*args, **kwargs)
        self.tree = get_tree()
        self.xml = get_xml_tree()

    def test_xpath(self):
        s = self.tree.xpath(
            '//div[@class="lst lst-1 new-list"]//li/span[2]/a/text()')
        #logger.debug('%s', s)
        self.assertIsNotNone(s)

    def test_index(self):
        s = self.tree.xpath(
            '//div[@class="lst lst-1 new-list"]//ul[2]//li[2]/span[2]/a/text()')
        # ???
        logger.debug('应该有页数个: %s', s)
        logger.debug('lst lst-1 new-list 个数 %s',
                     len(self.tree.xpath('//div[@class="lst lst-1 new-list"]')))
        self.assertIsNotNone(s)

    def test_xml_xpath(self):
        s = self.xml.xpath('//book[3]//author[1]')
        #logger.debug('应该只有一个: %s', s)
        self.assertIsNotNone(s)

    def test_split_index(self):
        s = self.tree.xpath(
            '//div[@class="lst lst-1 new-list"]//ul[2]//li[2]/span[2]/a/text()')
        div = self.tree.xpath('//div[@class="lst lst-1 new-list"]')
        self.assertEqual(len(div), 1)
        # Element 中使用xpath('./text()')
        uls = div[0].xpath('.//ul')
        self.assertEqual(len(uls), 30)

        lis = uls[1].xpath('.//li')
        self.assertEqual(len(lis), 9)

        spans = lis[1].xpath('./span')
        self.assertEqual(len(spans), 2)

        a = spans[1].xpath('./a')
        logger.debug('a = %s but %s', a[0].text, s[0])

        b1 = self.tree.xpath('//div[@class="lst lst-1 new-list"]//ul')
        b2 = self.tree.xpath('//div[@class="lst lst-1 new-list"]//ul[2]')
        b3 = self.tree.xpath('//div[@class="lst lst-1 new-list"]//ul[2]//li')
        b4 = self.tree.xpath(
            '//div[@class="lst lst-1 new-list"]//ul[2]//li[2]')
        b5 = self.tree.xpath(
            '//div[@class="lst lst-1 new-list"]//ul[2]//li[2]/span')
        b5 = self.tree.xpath(
            '//div[@class="lst lst-1 new-list"]//ul[2]//li[2]/span[2]')
        b6 = self.tree.xpath(
            '//div[@class="lst lst-1 new-list"]//ul[2]//li[2]/span[2]/a')

        show_list("b1", b1)
        show_list("b2", b2)
        show_list("b3", b3)
        show_list("b4", b4)
        show_list("b5", b5)
        show_list("b6", b6)


suite = unittest.TestLoader().loadTestsFromTestCase(XPathTest)
unittest.TextTestRunner(verbosity=2).run(suite)
