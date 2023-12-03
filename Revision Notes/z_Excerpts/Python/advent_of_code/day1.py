def part_1():
    formatted_var = []
    for i in lines:
        temp_var = ''
        for x in i:
            try:
                int(x)
                temp_var += str(x)
            except:
                pass
        if len(temp_var) == 1: 
            temp_var = temp_var + temp_var
        formatted_var.append(temp_var)

    output_var = 0
    for i in formatted_var:
        print(i)
        output_var += int(str(i[0]) + str(i[-1]))
    return output_var


def part_2():
    formatted_var = []
    global lines
    str_num = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    int_num = ['1', '2', '3', '4', '5', '6', '7, 8', '9']

    for i in range(0, len(lines)):
        temp_var = lines[i]
        print(temp_var)
        for x in range(0, 9):
            temp_var = temp_var.replace(str_num[x],int_num[x])
        print(temp_var)
        formatted_var[i] = temp_var
    
    lines = formatted_var
    formatted_var = []

    for i in lines:
        temp_var = ''
        for x in i:
            try:
                int(x)
                temp_var += str(x)
            except:
                pass
        if len(temp_var) == 1: 
            temp_var = temp_var + temp_var
        formatted_var.append(temp_var)

    output_var = 0
    for i in formatted_var:
        print(i)
        output_var += int(str(i[0]) + str(i[-1]))
    return output_var


filename_txt = '/Users/Alex/Documents/GitHub/rev_notes/Revision Notes/z_Excerpts/Python/advent_of_code/day1.txt'
f = open(filename_txt, 'r')
lines = f.readlines()

#print(part_1())
print(part_2())
