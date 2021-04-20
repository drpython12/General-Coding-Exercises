Number = 0
while (Number < 1) | (Number > 10):
    Number = int(input("Enter a positive whole number: "))
    if Number > 10:
        print("Number is too large")
    elif Number < 1:
        print("Not a positive number")
c = 1
for k in range(0, Number):
    print(c)
    c = int((c * (Number - 1 - k)) / (k + 1))