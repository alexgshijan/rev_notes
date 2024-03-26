def ordered_list_merge(list_a, list_b): # Merges two ordered list
    list_ab = []; list_ab_length_goal = len(list_a + list_b)

    while len(list_ab) != list_ab_length_goal:
        if list_a == [] and list_b == []: print('Logic Error')
        elif list_a == []: 
            for i in list_b: list_ab.append(i)
        elif list_b == []: 
            for i in list_a: list_ab.append(i)

        elif list_a[0] == list_b[0]: list_ab.append(list_a[0]); list_ab.append(list_b[0])
        elif list_a[0] > list_b[0]: list_ab.append(list_b[0]); del list_b[0]
        else: list_ab.append(list_a[0]); del list_a[0]
    return list_ab


list_input = [12,2,123213,4,314, 13213213, 12345, 124,56,2453245, 21313213213213,12312321321312,123123123123, 43535345,64754765,21313145363453667,253423234,4563546345] 
lists = [list_input[i: i+1] for i in range(0, len(list_input), 1)] # Seperates list into a list of lists of one value

while len(lists) != 1: # takes the first two lists, merges them using the ordered_list_merge function and append the merged lists onto the end of the list
    lists.append(ordered_list_merge(lists[0], lists[1])); del lists[1]; del lists[0]
lists = lists[0]
print(lists)


