from sys import stdin as s

s = open("input.txt", "rt")
""" 1436. 영화감독 숌 """

if __name__ == "__main__":
    n = int(s.readline().rstrip())

    ans = []


    for i in range(1, 200000000):
        s = str(i)

        if len(s.split("666")) >= 2:
            ans.append(int(s))
            
            if len(ans) - 1 == n:
                print(ans[-2])
                break