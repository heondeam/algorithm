""" 
분할정복 알고리즘

1. 분할 - 원래의 문제를 분할해서 비슷한 유형의 더 작은 하위 문제들로 나눈다.
2. 정복 - 하위 문제들을 각각 재귀적으로 해결한다.
3. 합치기 - 하위 문제들의 답을 합쳐서 원래의 문제를 해결한다.

"""

# 분할 정복 예시 1 (1부터 N까지의 합)

def consecutive_sum(start, end):
    if start == end:
        return start
    
    mid = (start + end) // 2
    
    return consecutive_sum(start, mid) + consecutive_sum(mid + 1, end)

# 분할 정복 예시 2 (합병정렬)

sub = [7,5,6,8,3,5,9,1]

def merge_sort(arr):
    # 원소개수가 1이면 그만 나눈다.
    if len(arr) <= 1:
        return arr

    # 항상 반으로 나눈다.
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    merged = merge(left, right)
    return merged

def merge(list1, list2):
    merged = []

    i = 0
    j = 0

    while len(list1) > 0 and len(list2) > 0:
        if list1[i] > list2[j]:
            merged.append(list2[j])
            del list2[j]
        else:
            merged.append(list1[i])
            del list1[i]

    if len(list1) > 0:
        merged += list1
    elif len(list2) > 0:
        merged += list2

    return merged

# 분할 정복 예시 3 (퀵 정렬)