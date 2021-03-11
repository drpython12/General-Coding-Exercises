# Letter matching question

first_word = str(input("Enter the first word: "))
second_word = str(input("Enter the second word: "))
common_letters = []
for x in first_word:
    if x in second_word:
        common_letters.append(x)
if (len(common_letters) == len(first_word)):
    print("First word can be formed from second word.")
else:
    print("First word cannot be formed from second word.")