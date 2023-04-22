# 정렬 알고리즘



# 버블 정렬 구현
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

# print(bubble_sort([65, 55, 45, 34, 25, 15, 10]))


# p.96 연습문제 4

def greatestNumber(array):
    greatestNumber = 0

    for i in array:
        if i > greatestNumber :
            greatestNumber = i

    return greatestNumber


# 선택 정렬 구현
def selection_sort(list):

    for i in range(len(list)):
        lowestNumberIndex = i

        for j in range(i + 1, len(list)):
            if list[j] < list[lowestNumberIndex]:
                lowestNumberIndex = j

        if lowestNumberIndex != i:
            temp = list[i]
            list[i] = list[lowestNumberIndex]
            list[lowestNumberIndex] = temp

    return list

# print(selection_sort([4, 2, 1, 7, 3]))


# 삽입 정렬 구현
def insertion_sort(array):
    for index in range(1, len(array)):

        temp_value = array[index]
        position = index - 1
    
        while position >= 0:
            if array[position] > temp_value:
                array[position + 1] = array[position]
                position = position - 1
            else:
                break
        
        array[position + 1] = temp_value

    return array


# 퀵 정렬 구현
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


new_arr = [32, 44, 11, 53, 87, 23, 66 , 12, 54, 72]


# print(quick_sort(new_arr))


# 계수 정렬 구현