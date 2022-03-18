import unittest
import requests

from rdflib import Graph, ConjunctiveGraph, compare
from yarrrml2rml import translate

class test_translate(unittest.TestCase):
    def test_convert_yarrrml2rml(self):
        print('ha ha')
        yarrrml = "/tests/yarrrml-input-test.yarrrml"
        rml_output = requests.post("http://127.0.0.1:5000/rmlconversion", data={'test': yarrrml})
        rml_output_path = open("/tests/rml-output-test.ttl", "w")
        rml_output_path.write(rml_output)

        expected_output_graph = ConjunctiveGraph()
        output_graph = ConjunctiveGraph()

        try:
            expected_output_graph.parse("/tests/mapping-expected.rml.ttl", format="turtle")
            output_graph.parse("/tests/mapping-output.rml.ttl", format="turtle")

            iso_expected = compare.to_isomorphic(expected_output_graph)
            iso_output = compare.to_isomorphic(output_graph)

            print('ha ha ha ha')
            # # and graphs are equal
            # if iso_expected == iso_output:
            #     result = "passed"
            # # and graphs are distinct
            # else:
            #     print("Output RDF does not match with the expected RDF")
            #     result = "failed"

            self.assertEqual(iso_output, iso_expected)
        except Exception as e:
            print(str(e))
            results = "failed"

if __name__ == '__main__':
    unittest.main()