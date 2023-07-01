from sys import stdin as s

s = open("input.txt", "rt")
""" 1449. 수리공 항승 """


if __name__ == "__main__":
    n, l = list(map(int, s.readline().rstrip().split()))
    pos = list(map(int, s.readline().rstrip().split()))
    pos.sort()

    e = 0
    index = 0

    for i in range(n):
        if pos[i] > e :
            e = pos[i] + l - 1
            index += 1
    
    print(index)