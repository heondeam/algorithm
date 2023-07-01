from sys import stdin as s
from itertools import combinations

s = open("input.txt", "rt")
""" 15903. 카드 합체 놀이 """

if __name__ == "__main__":
    n, m = list(map(int, s.readline().rstrip().split()))
    a = list(map(int, s.readline().rstrip().split()))

    # 2장의 카드를 서로 더해서 더한 값을 두 장의 카드에 덮어씀
    # m번 합체하고 놀이가 끝났을 때
    # 카드에 적혀있는 총합이 가장 적을때 출력
    # 정렬 후에 제일 작은 2개만 반복적으로 합체

    for _ in range(m):
        a = sorted(a)

        mSum = a[0] + a[1]

        a[0] = mSum
        a[1] = mSum
    
    print(sum(a))