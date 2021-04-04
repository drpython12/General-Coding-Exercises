def count(word):
    word_split = []
    for i in range(0, len(word)):
        word_split.append(word[i])
    return(word_split.count("-") + 1)
