from logging import exception
from draughtsman import parse
import apiRequest
import jsonschema
from jsonschema import validate
import json
import socketserver


base_URL = "https://fruitpal.doma.com/"
api_doc = "api-description.apib"


def request(http_verb,path,data,params):
    api_request = apiRequest.APIRequest(base_URL)
    # print(http_verb,path,data,params)
    response = api_request(http_verb,path,data=data,params=params)
    if response.status_code == 200:
        # print(response.json())
        return response.json()
    elif response.status_code == 401:
        return ({"error":"HTTP 401"})

def validateJson(jsonInstance,expSchemaFile):
        with open(expSchemaFile,'r') as file:
            expSchema = json.load(file)

        # print(expetedSchema)
        try:
            validate(instance=jsonInstance, schema=expSchema)
            return True, ""
        except Exception as err:
            # print(err)
            # errMsg = "Given JSON data is InValid"
            return False, err
        
def parseDoc(filename,transaction_type=None,endpoint=None,attrib=None):
    file = open(filename, 'r')
    parse_result = parse(file.read())

    for elem in parse_result.api.content:
        # req = elem.transitions[0].transactions[0].request.defract
        # response = elem.transitions[0].transactions[0].response.defract
        # if transaction_type == None:
        #     transaction_type = elem.transitions[0].transactions[0].request.method.defract
        # if endpoint == None:
        #     endpoint = elem.href.defract
        transaction_type = elem.transitions[0].transactions[0].request.method.defract
        endpoint = elem.href.defract

        if attrib == None:
            if 'hrefVariables' in elem.transitions[0].attributes.attributes:
                attrib = elem.transitions[0].attributes.attributes['hrefVariables'].defract
                # print(attrib)
                attrib = dict(attrib)
        
        req1 = request(transaction_type, endpoint, None, attrib)
        print(req1)
        res,errMsg = validateJson(req1,'expSchema.json')
        if res == False:
            print(errMsg)
            return req1, errMsg
    return req1

# Parse API doc
docToArgs = parseDoc(api_doc)