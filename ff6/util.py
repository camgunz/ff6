KNOWN_ABBREVIATIONS = [
    'hp',
    'mp',
    'xp',
    'gp',
]

def snake_to_camel(name):
    tokens = name.split('_')
    for n, token in enumerate(tokens):
        if token in KNOWN_ABBREVIATIONS:
            tokens[n] = token.upper()
        else:
            tokens[n] = token.capitalize()
    return ''.join(tokens)
