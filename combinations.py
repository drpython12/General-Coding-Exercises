## Combinations
## Objective: Take variable number of arguments and return the number of permutations 

def Combinations(f_arg, *argv):
    list1 = [f_arg]
    for arg in argv:
        list1.append(arg)
    product = 1
    for i in range(0, len(list1)):
        product = product * list1[i]
    return(product)

Combinations(2, 3, 4)