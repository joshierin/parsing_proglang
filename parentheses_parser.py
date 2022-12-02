def parse(tokens, parenthesis):
    retokens = []
    j = 0
    while j < len(tokens):
        token = tokens[j]
        if token.find(parenthesis) != -1:
            mini_tokens = token.split(parenthesis)
            if mini_tokens[0] != "":
                retokens.append(mini_tokens[0])
            retokens.append(parenthesis)
            if mini_tokens[1] != "":
                retokens.append(mini_tokens[1])
        else:
            retokens.append(token)
        j += 1
    return retokens