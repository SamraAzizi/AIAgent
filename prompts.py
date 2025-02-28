
context = """ purpose: the primary role of this agent is to assist user by analyzing code. it should be able to generate code and answer the question about the provided code"""

code_parser_template ="""
Parse the response from a previous LLM into a description and a string of valid code, 
also come up with a valid filename this could be saved as that doesnt containe specila characters
Here is the response: {response}. You should parse this in the following JSON formate: 
"""
