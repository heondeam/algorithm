# 이분탐색



arr = [1, 55, 2, 53, 22, 665, 90, 43]
arr.sort()

# 반복문을 이용한 이분탐색 구현
def binary_search_for(number):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if number == arr[mid]:
            # 찾는 숫자가 현재 중간 숫자일 때
            print("찾았다!")
            break
        elif number > arr[mid]:
            # 찾는 숫자가 현재 중간 숫자보다 클 때
            start = mid + 1
        else:
            # 찾는 숫자가 현재 중간 숫자보다 작을 때
            end = mid - 1


# 재귀를 이용한 이분탐색 구현
def binary_search_recur(list, target, start, end):
    mid = (start + end) // 2

    if start > end:
        print("못찾았다 ㅠㅠ")
        return

    if target == list[mid]:
        print("찾았다!")
        return
    elif target > list[mid]:
        binary_search_recur(list, target, mid + 1, end)
    else:
        binary_search_recur(list, target, start, mid - 1)


binary_search_recur(arr, 43, 0, len(arr) - 1)