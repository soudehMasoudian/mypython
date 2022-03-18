import unittest

from rdflib import Graph, ConjunctiveGraph, compare
from yarrrml2rml import translate

class test_translate(unittest.TestCase):
    def test_convert_yarrrml2rml(self):
        data = 