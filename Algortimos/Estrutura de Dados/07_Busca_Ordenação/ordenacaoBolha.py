def bubble_sort(a_list):
    for pass_num in range(len(a_list) - 1, 0, -1):
        for i in range(pass_num):
            print("Estou no segundo for")
            if a_list[i] > a_list[i + 1]:
                temp = a_list[i]
                a_list[i] = a_list[i + 1]
                a_list[i + 1] = temp


#a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
a_list = [1, 2, 3, 4, 5, 6]
bubble_sort(a_list)
print(a_list)
