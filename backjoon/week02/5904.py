from sys import stdin as s

s = open("input.txt", "rt")
""" 
문제
"""
def moo_length(k):
    if k == 0:
        return 3
    else:
        return 2 * moo_length(k-1) + (k + 3)
    
def recur(n, k, leng_arr):
    if k == 0:
        return 'm' if n == 1 else 'o'
    
    lt = (leng[k] - (k + 3)) // 2 # 좌측 S(k-1)의 길이
    rt = lt + k + 3  # 우측 S(k-1)의 길이

    if 1 <= n <= lt:
        return recur(n, k - 1, leng_arr)
    elif lt + 1 <= n <= rt:
        return 'm' if n == lt + 1 else 'o'
    else:
        return recur(n - rt, k - 1, leng_arr)

if __name__ == "__main__":
    # 1 <= n <= 10 ^9
    # 완전탐색 X, 분할 정복? 이분 탐색?
    n = int(s.readline().rstrip())

    cnt = 1
    leng = [3]
    s = 0

    # 10 ^ 9 까지에 해당하는 s(k)의 길이를 구한다
    while leng[-1] <= (10 ** 9):
        leng.append(moo_length(cnt))
        cnt += 1

    for i in range(len(leng)):
        if leng[i] >= n:
            s = i
            break

    print(recur(n, s, leng))