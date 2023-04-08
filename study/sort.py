# 정렬 알고리즘



# 버블정렬 구현
def bubble_sort(list):
    last_index = len(list) - 1
    isSorted = False

    while not isSorted:
        isSorted = True

        for i in range(last_index):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                isSorted = False
        last_index -= 1

    return list

print(bubble_sort([65, 55, 45, 34, 25, 15, 10]))