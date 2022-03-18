# dependencies related to api
from translate_yarrrml2rml import translate
from flask import Flask, request 
import yaml

app = Flask(__name__)


# we used pretty-yarrrml2rml lib, but since it has some errors
# in validation part, so we overridden this method to resolve
# the problem

@app.route('/restrmlconversion', methods=['POST'])
def translate_http_request():
    print("------------------------START TRANSLATING HTTP REQUEST YARRRML TO RML-------------------------------")

    yarrrml_data = yaml.safe_load(request.values['test'])

    print("yarrrm: ", yarrrml_data)

    return translate(yarrrml_data)

@app.route('/filermlconversion', methods=['POST'])
def translate_file_request():
    print("------------------------START TRANSLATING HTTP REQUEST YARRRML TO RML-------------------------------")

    yarrrml_data = open("./tests/yarrrml-input-test.yml").read()
    payload = {'test': yarrrml_data}

    print("yarrrm: ", payload)

    return translate(payload)


#print(translate(yaml.safe_load(open("mapping.yml"))))
app.run()