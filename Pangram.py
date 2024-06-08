import string
def is_pangram(sentence):
    sentence = sentence.lower()
    alphabet_set = set(string.ascii_lowercase)
    sentence_set = set(sentence)   
    return alphabet_set.issubset(sentence_set)
