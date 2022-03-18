import unittest
import requests

# from yarrrml2rml import translate
# end-to-end test
class test_yarrrml2rml(unittest.TestCase):
    def test_translate(self):
        # subprocess.Popen('translate_yarrrml2rml')
        
        yarrrml = open("./tests/yarrrml-input-test.yml", "r").read()
        payload = {'yarrrml': yarrrml}
        yarrrml.close()
        rml_output = requests.post("http://127.0.0.1:5000/rmlconversion", payload)
        rml_output_path = open("./tests/rml-output-test.ttl", "w")
        rml_output_path.write(rml_output.text)
        rml_output_path.flush()
        rml_output_path.close

        try:
            expected_output = open("./tests/mapping-expected.rml.ttl").read()
            output = open("./tests/rml-output-test.ttl").read()
            
            self.assertEqual(expected_output, output)
            
        except Exception as e:
            print(str(e))
            results = "failed"
        
        

if __name__ == '__main__':
    unittest.main()