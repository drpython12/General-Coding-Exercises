def is_anagram(word1, word2):
    word1.lower()
    word2.lower()
    if sorted(word1) == sorted(word2):
        return(True)
    else:
        return(False)