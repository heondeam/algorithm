from sys import stdin as s
from itertools import permutations

s = open("input.txt", "rt")
""" 2309. 일곱 난쟁이 """

if __name__ == "__main__":
    shorters = [int(s.readline().rstrip()) for _ in range(9)]

    # 서로 다른 9개에서 7개를 뽑는 경우의 수
    arr = list(permutations(shorters, 7))

    for s in arr:
        tmp = []

        if sum(s) == 100:   
            print(*sorted(s), sep="\n")
            break