from sys import stdin as s
from itertools import permutations

s = open("input.txt", "rt")
""" 2503. 숫자 야구 """

# 민혁이 말한 숫자 123
# 영수 1 스트라이크 1볼
# 민혁이 말한 숫자 356
# 영수 1 스트라이크 0볼
# 민혁이 말할 숫자 327
# 영수 2 스트라이크 0볼
# 민혁이 말한 숫자 489
# 영수 0 스트라이크 1볼

# 영수가 생각하고 있을 답의 총 개수를 출력하자

if __name__ == "__main__":
    n = int(s.readline().rstrip())
    context = [list(map(int, s.readline().rstrip().split())) for _ in range(n)]

    arr = list(permutations([1,2,3,4,5,6,7,8,9], 3))

    for i in range(n):
        q, s, b = context[i]
        q = [int(a) for a in str(q)]
        remove_cnt = 0

        for i in range(len(arr)):
            s_cnt, b_cnt = 0, 0

            i -= remove_cnt

            for j in range(3):
                if q[j] in arr[i]:
                    if j == arr[i].index(q[j]):
                        s_cnt += 1
                    else: 
                        b_cnt += 1

            if s_cnt != s or b_cnt != b:
                arr.remove(arr[i])
                remove_cnt += 1

    print(len(arr))