def MiddleString(word):
    middleIndex = int(len(word) / 2)
    print("Original string is " + word)
    middleThree = word[middleIndex-1:middleIndex+2]
    print("Middle three letters are " + middleThree)

def AppendStrings(s1, s2):
    middleIndex = int(len(s1) / 2)
    print(s1[0:middleIndex] + s2 + s1[middleIndex:])

def ExerciseThree(s1, s2):
    middleIndex1 = int(len(s1) / 2)
    middleIndex2 = int(len(s2) / 2)
    print(s1[0] + s2[0] + s1[middleIndex1] + s2[middleIndex2] + s1[len(s1) - 1] + s2[len(s2) - 1])

def ExerciseFour(word):
    lower = []
    upper = []
    for i in range(0, len(word) - 1):
        if word[i].islower():
            lower.append(word[i])
        elif word[i].isupper():
            upper.append(word[i])

    lowercase = ""
    uppercase = ""
    print(lowercase.join(lower) + uppercase.join(upper))