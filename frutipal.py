from draughtsman import parse
import apiRequest
import requests


base_URL = "https://fruitpal.doma.com/"
def request(http_verb,path,data,params):
    api_request = apiRequest.APIRequest(base_URL)
    print(http_verb,path,data,params)
    response = api_request(http_verb,path,data=data,params=params)
    if response.status_code == 200:
        print(response.json())
    
# from refract.elements.primitives import String

file = open("api-description.apib", 'r')
parse_result = parse(file.read())

for elem in parse_result.api.content:
    # req = elem.transitions[0].transactions[0].request.defract
    response = elem.transitions[0].transactions[0].response.defract
    transaction_type = elem.transitions[0].transactions[0].request.method.defract
    endpoint = elem.href.defract
    if 'hrefVariables' in elem.transitions[0].attributes.attributes:
        attrib = elem.transitions[0].attributes.attributes['hrefVariables'].defract
        print(attrib)
        attrib = dict(attrib)
    else:
        attrib = None
    
    
    req1 = request(transaction_type, endpoint, None, attrib)
    print(req1)


    #print request and response

    # print("transaction_type= ", transaction_type)
    # print("endpoint= ", endpoint)
    # print("Attributes= ", attrib)
    # print("Request= ", request)
    print("Response= ", response)

# print("Basic API defract")

# print(parse_result.api.defract)

# # print("annotations")
# # print(parse_result.annotations)
# print("resources")
# print(parse_result.api.resources)
# print("content")
# print(parse_result.content)
# print("children")
# print(parse_result.api.children.pop())
# print("children")
# print(parse_result.api.transitions)
# print(parse_result.api.title.defract)
# print("Title defract")
# print(parse_result.api.title.attributes.get('sourcemap'))
# print(parse_result.api.content.pop().defract)
# print(parse_result.api.content.pop().defract)
# elem1 = parse_result.api.content.pop(-1)
# print(elem1.href.defract)
# endpoint = []

# print(endpoint)
# FORMAT: 1A
# GET /commodities
# + Response 200 (application/json)

#       {"COMMODITIES":["mango","pineapple","apple"]}
# # GET /prices?commodity=pineapple&price_per_trade=100&volume_in_tons=1

# + Response 200 (application/json)

#       {"PRICES":[{"COST":"102.58","COUNTRY":"BR"}]}
# )




# from markdown import Markdown
# m = Markdown(extensions=["plueprint"])
# m.set_output_format("apiblueprint")
# api = m.convert("""
# FORMAT: 1A

# # GET /commodities
# + Response 200 (application/json)

#       {"COMMODITIES":["mango","pineapple","apple"]}
# # GET /prices?commodity=pineapple&price_per_trade=100&volume_in_tons=1

# + Response 200 (application/json)

#       {"PRICES":[{"COST":"102.58","COUNTRY":"BR"}]}
# """)
# print(api)



# FORMAT: 1A

# # The Simplest API
# This is one of the simplest APIs written in the **API Blueprint**.

# # /message

# ## GET
# + Response 200 (text/plain)

#         Hello World! 

# api = '# My AAPI git1'
# # parse_result = parse(api)
# # print(parse_result.api.title.defract)
# api = '# My AAPI git'
# parse_result = parse(api)
# print(parse_result.api.title.defract)