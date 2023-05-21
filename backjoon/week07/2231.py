from sys import stdin as s

s = open("input.txt", "rt")
""" 2231. 분해합 """

if __name__ == "__main__":
    n = int(s.readline().rstrip())
    ans = []

    for i in range(1, 1000001):
        tmp = i

        for j in str(i):
            tmp += int(j)

        if tmp == n:
            ans.append(i)

    
    if ans:
        print(min(ans))
    else:
        print(0)