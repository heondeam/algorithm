from sys import stdin as s
from itertools import combinations_with_replacement

s = open("input.txt", "rt")
""" 10448. 유레카 이론 """

if __name__ == "__main__":
    t = int(s.readline().rstrip())

    for i in range(t):
        k = int(s.readline().rstrip())

        T = []

        flag = 0

        for j in range(1, k + 1):
            if (j * (j + 1) // 2) >= k:
                break
            else:
                T.append(j * (j + 1) // 2)

        arr = list(combinations_with_replacement(T, 3))

        for n in arr:
            if sum(n) == k:
                flag =1
                break

        print(flag)