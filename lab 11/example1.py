def SelectionSort(list: list):
    if len(list) == 1:
        return list
    else:
        for indexes in list:
            if indexes < list[0]:
                list.remove(indexes)
                list.insert(0, indexes)
        return [list[0]] + SelectionSort(list[1:])


print(SelectionSort([43, 342, 343, 2, 34, 34]))
