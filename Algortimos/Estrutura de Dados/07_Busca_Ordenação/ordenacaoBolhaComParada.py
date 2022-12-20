def short_bubble_sort(a_list):
    exchanges = True
    pass_num = len(a_list) - 1
    while pass_num > 0 and exchanges:
        exchanges = False
        for i in range(pass_num):
            print("Estou no laço for")
            if a_list[i] > a_list[i + 1]:
                exchanges = True
                print("Houve troca")
                temp = a_list[i]
                a_list[i] = a_list[i + 1]
                a_list[i + 1] = temp
        if exchanges:
            print("Houveram trocas")
        else:
            print("Não houveram trocas")

        pass_num = pass_num - 1


#a_list = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
a_list = [1, 2, 3, 4, 5, 6]
short_bubble_sort(a_list)
print(a_list)
