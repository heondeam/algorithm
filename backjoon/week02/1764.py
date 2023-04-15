from sys import stdin as s

s = open("input.txt", "rt")
""" 
문제

김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 
듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.

첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다. 
이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과,
N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다. 
이름은 띄어쓰기 없이 알파벳 소문자로만 이루어지며, 그 길이는 20 이하이다.
N, M은 500,000 이하의 자연수이다.

듣도 못한 사람의 명단에는 중복되는 이름이 없으며, 보도 못한 사람의 명단도 마찬가지이다.
"""

N, M = list(map(int, s.readline().split()))
persons = [s.readline().rstrip() for _ in range(N + M)]

dlp = persons[:N]
dsp = persons[N:N+M]

my_table = {}

for p in dlp:
    my_table[p] = 1

for p in dsp:
    if p in my_table:
        my_table[p] += 1
    else:
        my_table[p] = 1

cnt = 0
ans = []

for a in my_table:
    if my_table[a] >= 2:
        cnt += 1
        ans.append(a)
else:
    print(cnt)

    ans.sort()
    for k in ans:
        print(k)
