def part_1(red, green, blue):
    accum = 0
    for i in lines:
        red_var = 0
        green_var = 0
        blue_var = 0
        
        temp_var = i[7:]
        temp_list_var = temp_var.split(';')

        for x in temp_list_var:
            for j in x.split(','):
                if j[-1] == 'd': 
                    print(red_var)
                    if (int(j[1:3]) > int(red_var)): 
                        red_var = j[1:3]
                        print(j[1:3])
                        print(red_var)

                elif j[-1] == 'n': 
                    if int(j[1]) > int(green_var): 
                        green_var = j[1]

                elif j[-1] == 'e': 
                    if int(j[1]) > int(blue_var): 
                        blue_var = j[1]

        if ((int(red) >= int(red_var)) and (int(green) >= int(green_var)) and (int(blue) >= int(blue_var))):
            accum += int(i[5])
    return accum


def part_2():
    pass



filename_txt = '/Users/Alex/Documents/GitHub/rev_notes/Revision Notes/z_Excerpts/Python/advent_of_code/day2.txt'
f = open(filename_txt, 'r')
lines = f.readlines()

print(part_1(12,13,14))