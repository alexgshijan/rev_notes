def pivot_orient(list_values): # Pivot splits the list using the first list entry
    pivot = list_values[0]
    pivot_tracker = 0
    for i in range(1, len(list_values)):
        if list_values[i] > pivot:
            pass
        else:
            list_values.insert(0, list_values[i])
            del list_values[i+1]
            pivot_tracker += 1
    return [list_values[:pivot_tracker], list_values[pivot_tracker:]]


input_list = [3,1, 6, 2, 1]

lists = [input_list]
while len(lists[0]) > 2:
    tmp_list_val = pivot_orient(lists[0])
    del lists[0]
    lists.append(tmp_list_val[0])
    lists.append(tmp_list_val[1])
    print (lists)
print(lists)