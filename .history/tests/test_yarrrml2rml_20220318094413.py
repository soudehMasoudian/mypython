import unittest
import requests

# from yarrrml2rml import translate
# end-to-end test
class test_yarrrmltorml(unittest.TestCase):
    def test_translate(self):        
        yarrrml = open("./tests/yarrrml-input-test.yml").read()
        payload = {'yarrrml': yarrrml}
        rml_output = requests.post("http://0.0.0.0:5000/rmlconversion", payload)

        try:
            expected_output = open("./tests/mapping-expected.rml.ttl").read()            
            self.assertEqual(expected_output, rml_output.text)
            
        except Exception as e:
            print(str(e))
            results = "failed"
        
        

if __name__ == '__main__':
    unittest.main()