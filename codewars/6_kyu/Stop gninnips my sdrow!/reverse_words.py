def spin_words(sentence):
    if len(sentence) == 0:
        return ''
    og_words = sentence.split(" ")
    
    for index, word in enumerate(og_words):
        if len(word) >= 5:
            og_words[index] = reverse(word)
            
    return " ".join(word for word in og_words)
          
    
def reverse(word):
    len_word = len(word)
    res = ""
    
    for index in range(1, len_word + 1):
        res += word[-index]
    
    return res