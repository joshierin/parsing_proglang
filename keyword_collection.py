def collect_keywords(keywords, tokens):
    source_code_keywords = []

    for token in tokens:
        if token in keywords:
            source_code_keywords.append(token)
        
    print("Keywords detected!")
    print(source_code_keywords)