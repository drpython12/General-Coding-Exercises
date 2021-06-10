def is_curzon(x):
    if (2**x + 1) % (2*x + 1) == 0:
        print("True")
    else:
        print("False")

is_curzon(int(input("Enter a number: ")))