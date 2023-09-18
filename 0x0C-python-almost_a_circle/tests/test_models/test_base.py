#!/usr/bin/python3
""" 0-main """
import unittest

from models.base import Base

class TestBase(unittest.TestCase):
    def test_inc1(self):
        assert(Base().id) == 1

    def test_inc2(self):
        assert(Base().id) == 2

    def test_inc3(self):
        assert(Base().id) == 3

    def test_inc4(self):
        assert(Base(12).id) == 12

    def test_inc5(self):
        assert(Base().id) == 4
