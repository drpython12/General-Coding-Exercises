def flatten(lists):
    result = []
    for i in lists:
        for x in i:
            result.append(x)
    return(result)

flatten([[1, 2], [3, 4]])