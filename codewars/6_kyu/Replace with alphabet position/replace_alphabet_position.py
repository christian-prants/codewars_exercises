import string, re

def alphabet_position(text):
    n_str = []

    text = re.sub('[^a-z]', '', text.lower())

    for number in text:   
        n_str.append(string.ascii_lowercase.index(number) + 1)

    return ' '.join(str(x) for x in n_str)