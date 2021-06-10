def Stutter(x):
    word = []
    for i in range(0, len(x)):
        word.append(x[i])
    
    print(word[0] + word[1] + "...", word[0] + word[1] + "...", x)

word = str(input("Enter a word: "))
Stutter(word)