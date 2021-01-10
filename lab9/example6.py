def PascalTriangle(n):
    if n == 1:
        ReturnedList = [[1]]
        return ReturnedList
    else:
        predetermined = [1, 1] 
        nestedList = PascalTriangle(n - 1)
        calculation = nestedList[-1]
        for index in range(len(calculation) - 1):
            predetermined.insert(1, calculation[index] + calculation[index + 1])
        nestedList.append(predetermined)
    return nestedList