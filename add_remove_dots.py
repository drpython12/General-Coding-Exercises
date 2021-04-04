def add_dots(word):
    word_split = []
    for i in range(0, len(word)):
        word_split.append(word[i])
    return(".".join(word_split))
    
def remove_dots(word):
    return(word.replace(".", ""))    