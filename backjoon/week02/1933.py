from sys import stdin as s
import heapq

s = open("input.txt", "rt")

""" 
문제

N개의 직사각형 모양의 건물들이 주어졌을 때, 
스카이라인을 구해내는 프로그램을 작성하시오. 
스카이라인은 건물 전체의 윤곽을 의미한다. 
즉, 각각의 건물을 직사각형으로 표현했을 때, 
그러한 직사각형들의 합집합을 구하는 문제이다.

예를 들어 직사각형 모양의 건물들이 위와 같이 주어졌다고 하자. 
각각의 건물은 왼쪽 x좌표와 오른쪽 x좌표, 그리고 높이로 나타난다.
모든 건물들은 편의상 같은 높이의 지면(땅) 위에 있다고 가정하자. 
위의 예에서 스카이라인을 구하면 아래와 같다.

첫째 줄에 건물의 개수 N(1 ≤ N ≤ 100,000)이 주어진다. 
다음 N개의 줄에는 N개의 건물에 대한 정보가 주어진다. 
건물에 대한 정보는 세 정수 L, H, R로 나타나는데, 
각각 건물의 왼쪽 x좌표, 높이, 오른쪽 x좌표를 의미한다. 
(1 ≤ L < R ≤ 1,000,000,000, 1 ≤ H ≤ 1,000,000,000)

첫째 줄에 스카이라인을 출력한다. 
출력을 할 때에는 높이가 변하는 지점에 대해서, 그 지점의 x좌표와 그 지점에서의 높이를 출력한다.
"""
n = int(s.readline().rstrip())
buildings = [list(map(int, s.readline().rstrip().split())) for _ in range(n)]

arr = []
height = [0] * n
q = []

# end : 현재 index번째 건물의 끝나는 지점을 저장하는 리스트이다.
end = [0] * n
# check : 현재까지 끝난 끝점을 저장하는 set
check = set()

for i in range(n):
    l, h, r = map(int, buildings[i])

    # 시작점일 경우 1, 끝점일 경우 -1
    arr.append((l, i, 1))
    arr.append((r, i, -1))
    height[i] = h
    end[i] = r

# 정렬해준다.
# 첫번째 우선순위 : 시점이 앞서는가?
# 두번째 우선순위 : 시점이 같다면 시작점인가?
# 세번째 우선순의 : 시점도 같고 둘 다 시작점이라면 높이가 더 높은가?
arr.sort(key=lambda x: (x[0], -x[2], -height[x[1]]))

# now : 현재 최고 높이
now = 0
ans = []

for i in range(len(arr)):
    # point : 시점, idx: 건물의 인덱스, dir: 시작점인지 끝점인지
    point, idx, dir = arr[i]

    # 시작점인 경우
    if dir == 1:
        # 높이가 갱신된다면 그 부분이 새로운 스카이라인이 된다.
        if now < height[idx]:
            now = height[idx]
            ans.append((point, now))
        
        # 높이가 갱신됨과 상관없이 현재 건물의 높이와 끝점을 최대 힙에 저장한다.
        heapq.heappush(q, (-height[idx], end[idx]))
    
    # 끝점인 경우
    else:
        # 현재 시점이 끝났기 때문에 set에 끝점의 시점을 저장한다.
        check.add(point)
        # 최대 높이가 끝난 건물이 아닌때까지 pop
        while q:
            if q[0][1] not in check:
                break
            heapq.heappop(q)

        # 힙이 비었다면 스카이라인의 높이는 0으로 갱신한다.
        if not q:
            if now: 
                now = 0
                ans.append((point, now))

        # 힙이 있다면 현재 높이와 비교 시 변동이 있다면 그 높이가 그 다음으로 높은 건물이기 때문에
        # 스카이라인 높이 갱신
        else:
            if -q[0][0] != now:
                now = -q[0][0]
                ans.append((point, now))

# 정답 출력
for i in ans:
    print(i[0], i[1], end=" ")