### Programming Assessment 2: Question 2

numberIn = int(input("Enter a positive whole number: "))
numberOut = 0
count = 0
while numberIn > 0:
    count = count + 1
    partValue = numberIn % 2
    numberIn = numberIn // 2
    for i in range(1, count):
        partValue = partValue * 10
    numberOut += partValue
print("The result is:", numberOut)