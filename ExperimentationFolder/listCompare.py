lsta = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
lstb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
def difference(lsta, lstb):
    new_list = []
    for i in lsta:
        if i not in lstb:
            new_list.append(i)

    for j in lstb:
        if j not in lsta:
            new_list.append(j)
    return (new_list)
print(sorted(difference(lsta,lstb)))

