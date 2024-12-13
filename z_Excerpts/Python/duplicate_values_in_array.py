sorted_list = [1,1,2,2,2,2,3,4,5,6,6,6,7]
found = False

for i in range(0, len(sorted_list)-1):
    if sorted_list[i] == sorted_list[i+1]:
        print(f"Found in index {i+1}")
        found = True

print(f"Found is {found}")