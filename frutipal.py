from draughtsman import parse

api = '# My AAPI'
parse_result = parse(api)
print(parse_result.api.title.defract)

api1= """#FORMAT: 1A
# # GET /commodities
# + Response 200 (application/json)

# # GET /prices?commodity=pineapple&price_per_trade=100&volume_in_tons=1

# + Response 200 (application/json)

#      {"PRICES":[{"COST":"102.58","COUNTRY":"BR"}]}
"""
parse_result = parse(api1)
print(parse_result.api.title.defract)
print(parse_result.api.defract)

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
