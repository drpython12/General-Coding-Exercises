def mid(word):
    if (len(word) % 2) != 0:
        i = int(len(word)/2)
        return(word[i])
    else:
        return("")

mid("aaaa")