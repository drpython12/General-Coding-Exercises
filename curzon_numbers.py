## Curzon Numbers
## Objective: Establish if a given integer is a curzon number

def IsCurzon(x):
    num = int(x)
    if ((2**num + 1) % (2*num + 1)) == 0:
        print("True")
    else:
        print("False")

IsCurzon(10)