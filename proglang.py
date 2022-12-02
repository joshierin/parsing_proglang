import keyword_collection
import java_keywords
import parentheses_parser

def indent(indent_count):
    return "\t" * indent_count
    
# filepath = input('Please enter source code file path: ')
filepath = "D:\Parsing Project\HelloWorld.java"
file = open(filepath, "r") # open file 
source_code = file.read() # read file contents

tokens = source_code.split() # split user input separated by white spaces 
print("tokens after split:")
print(tokens, "\n")

tokens = parentheses_parser.parse(tokens, "(") # parse string with open parentheses
print("tokens after parsing opening parentheses:")
print(tokens, "\n")

tokens = parentheses_parser.parse(tokens, ")") # parse string with close parentheses
print("tokens after parsing closing parentheses:")
print(tokens, "\n")


i = 0
indent_count = 0

while i < len(tokens):
    token = tokens[i]
    if token == "{": 
        print("\n" + indent(indent_count) + token)
        indent_count += 1
        print(indent(indent_count) + tokens[i + 1], end = " ")
        i += 1
    elif token == "}":
        indent_count -= 1
        print("\n" + indent(indent_count) + token)
    elif token == "if":
        print("\n" + indent(indent_count) + token, end = " ")
    elif token == "else":
        print("\n" + indent(indent_count) + token, end = " ")
    else:
        print(token, end = " ")
    
    i += 1
    
keyword_collection.collect_keywords(java_keywords.keywords, tokens)

#        Group 1 
#   Gene Caleb Carbonilla
#  Xyphrus Von Keith Caguan
#      Joshreen Reyes
#     Jirah Kate Solano
#        BSCS-4A