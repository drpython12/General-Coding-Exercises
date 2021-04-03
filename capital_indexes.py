def CapitalIndexes(word):
    index_list = []
    enumerate(word)
    for i in range(0, len(word)):
        if word[i].isupper():
            index_list.append(i)
    return(index_list)

CapitalIndexes("HeLlO")