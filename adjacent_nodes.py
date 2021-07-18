## Finding Adjacent Nodes
## Objective: Determine if two nodes are adjacent when you are given the matrix and the two nodes

def Adjacent(x, y):
    matrix = [
        [0, 1, 0, 0],
        [1, 0, 1, 1],
        [0, 1, 0, 1],
        [0, 1, 1, 0]
    ]
    if matrix[x][y] == 1:
        print("True")
    else:
        print("False")

Adjacent(0, 2)