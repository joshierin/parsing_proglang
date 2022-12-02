def parse_opening(tokens):
    retokens = []
    j = 0
    while j < len(tokens):
        token = tokens[j]
        if token.find("(") != -1:
            mini_tokens = token.split("(")
            if mini_tokens[0] != "":
                retokens.append(mini_tokens[0])
            retokens.append("(")
            if mini_tokens[1] != "":
                retokens.append(mini_tokens[1])
        else:
            retokens.append(token)
        j += 1
    return retokens

def parse_closing(tokens):
    retokens = []
    h = 0
    while h < len(tokens):
        token = tokens[h]
        if token.find(")") != -1:
            mini_tokens = token.split(")")
            if mini_tokens[0] != "":
                retokens.append(mini_tokens[0])
            retokens.append(")")
            if mini_tokens[1] != "":
                retokens.append(mini_tokens[1])
        else:
            retokens.append(token)
        h += 1
    return retokens