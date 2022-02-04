my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
pos = []
j = 0

for i in my_list:
    while j <= len(my_list):
        if i == my_list[j]:
            # pos.append(j)
            print(i, j, my_list[j])
            j = j + 1
    # print(pos)
    # del pos[:]
