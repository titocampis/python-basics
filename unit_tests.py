from datetime import datetime
from unittest import TestCase
import unittest

from services import pingto


# Test Unitario para Tests de Ping
class TestPing(TestCase):
    def test_correct_ping(self):
        self.assertTrue(pingto('100','www.google.es')[0])
    def test_incorrect_ping(self):
        self.assertFalse(pingto('100','www.googlestio.es')[0])

unittest.main()