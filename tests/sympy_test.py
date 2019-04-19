#! /usr/bin/env python
#! -*- coding: utf-8 -*-

from sympy import *
import logging
import unittest
import sys

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    handlers=[
                        logging.StreamHandler(sys.stdout)
                    ])

logger = logging.getLogger(__name__)


class SympyTest(unittest.TestCase):

    def test_solve(self):
        x = Symbol('x')
        y = Symbol('y')
        r = solve([x + y - 3, x - y - 1], [x, y])
        logger.debug("test_solve: %s", r)
        self.assertEqual(2, r[x])
        self.assertEqual(1, r[y])

    def test_limit(self):
        n = Symbol('n')
        s = ((n+3)/(n+2))**n
        r = limit(s, n, oo)
        logger.debug("test_limit: %s", r)
        self.assertEqual(E, r)

    def test_integrate(self):
        t = Symbol('t')
        x = Symbol('x')
        m = integrate(sin(t)/(pi-t), (t, 0, x))
        n = integrate(m, (x, 0, pi))
        logger.debug("test_integrate: %s", n)

    def test_diff(self):
        f = Function('f')
        x = Symbol('x')
        r = dsolve(diff(f(x), x) - 2*f(x)*x, f(x))
        logger.debug("test_diff: %s", r)

    def test_no_eq(self):
        x = Symbol('x', real=True)
        y = Symbol('y', real=True)
        r = reduce_inequalities(0 <= x + y*2 - 1, [x])
        logger.debug("test_no_eq: %s", r)

    def test_solve2(self):
        l, m, n = symbols('l m n', integer=True)
        k = Symbol('k', real=True)
        init_printing(use_unicode=True)
        r = solve(
            [l/(1+exp(k * m)) + n,
             l/(1+exp((k * m) - 20 * k)) + n - 10000,
             l/(1+exp((k * m) - 80 * k)) + n - 80000],
            (l, m, n, k), dict=True)
        logger.debug("test_solve2: %s", r)

    def test_solve3(self):
        l, m, n = symbols('l m n', integer=True)
        k = Symbol('k', real=True)
        init_printing(use_unicode=True)
        r = solve(
            [l/(1+exp(k * m)) + n,
             l/(1+exp((k * m) - 5 * k)) + c - 500,
             l/(1+exp((k * m) - 20 * k)) + n - 10000,
             l/(1+exp((k * m) - 80 * k)) + n - 80000],
            [l, m, n, k], dict=True)
        logger.debug("test_solve3: %s", r)


suite = unittest.TestLoader().loadTestsFromTestCase(SympyTest)
unittest.TextTestRunner(verbosity=2).run(suite)
