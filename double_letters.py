def double_letters(word):
    count = 0
    for i in range(0, len(word) - 1):
            if word[i] == word[i+1]:
                count += 1
    if count == 1:
        return(True)
    else:
        return(False)

double_letters("hello")