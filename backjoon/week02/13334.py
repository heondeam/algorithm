from sys import stdin as s
import heapq

s = open("input.txt", "rt")

""" 
문제

집과 사무실을 통근하는 n명의 사람들이 있다. 
각 사람의 집과 사무실은 수평선 상에 있는 서로 다른 점에 위치하고 있다. 
임의의 두 사람 A, B에 대하여, A의 집 혹은 사무실의 위치가 B의 집 혹은 사무실의 위치와 같을 수 있다. 
통근을 하는 사람들의 편의를 위하여 일직선 상의 어떤 두 점을 잇는 철로를 건설하여, 기차를 운행하려고 한다. 
제한된 예산 때문에, 철로의 길이는 d로 정해져 있다. 
집과 사무실의 위치 모두 철로 선분에 포함되는 사람들의 수가 최대가 되도록, 철로 선분을 정하고자 한다.

양의 정수 d와 n 개의 정수쌍, (hi, oi), 1 ≤ i ≤ n,이 주어져 있다. 
여기서 hi와 oi는 사람 i의 집과 사무실의 위치이다. 
길이 d의 모든 선분 L에 대하여, 집과 사무실의 위치가 모두 L에 포함되는 사람들의 최대 수를 구하는 프로그램을 작성하시오

그림 1. 8 명의 집과 사무실의 위치
그림 1 에 있는 예를 고려해보자. 
여기서 n = 8, 
(h1, o1) = (5, 40), 
(h2, o2) = (35, 25), 
(h3, o3) = (10, 20),
(h4, o4) = (10, 25), 
(h5, o5) = (30, 50),
(h6, o6) = (50, 60), 
(h7, o7) = (30, 25), 
(h8, o8) = (80, 100)이고, 
d = 30이다. 이 예에서, 
위치 10 과 40 사이의 빨간색 선분 L이, 
가장 많은 사람들에 대하여 집과 사무실 위치 모두 포함되는 선분 중 하나이다. 따라서 답은 4 이다.

입력은 표준입력을 사용한다. 
첫 번째 줄에 사람 수를 나타내는 양의 정수 n (1 ≤ n ≤ 100,000)이 주어진다. 
다음 n개의 각 줄에 정수 쌍 (hi, oi)가 주어진다. 
여기서 hi와 oi는 −100,000,000이상, 100,000,000이하의 서로 다른 정수이다. 
마지막 줄에, 철로의 길이를 나타내는 정수 d (1 ≤ d ≤ 200,000,000)가 주어진다.

출력은 표준출력을 사용한다. 길이 d의 임의의 선분에 대하여, 집과 사무실 위치가 모두 그 선분에 포함되는 사람들의 최대 수를 한 줄에 출력한다. 
"""
n = int((s.readline().rstrip()))
input_data = [a.rsplit()  for a in s.readlines()]
positions = [list(map(int, a)) for a in input_data[:n]]
L = int(input_data[-1][0])
roads = []

# 각 위치들을 오름차순 정렬.
positions.sort()

# 각 위치별 사무실 - 집 거리가 L 보다 작거나 같다면 roads에 추가
for i in range(n):
    if abs(positions[i][0] - positions[i][1]) <= L:
        roads.append(positions[i])

# L에 포함될 수 있는 포지션들을 모아놓은 roads를 사무실 위치를 기준으로 오름차순 정렬
roads.sort(key=lambda x: x[1])

# 우선순위 큐와 정답 변수 선언
answer = 0
q = []

for road in roads:
    if not q:
        # 우선순위 큐가 비어있다면 일단 push
        heapq.heappush(q, road)
    else:
        # 원소가 존재 한다면? 사무실 위치에서 L을 뺐을 때 큐의 최솟값 보다 크다면 반복문 시작
        while q[0][0] < road[1] - L:
            heapq.heappop(q)
            if not q:
                break

        heapq.heappush(q, road)
    answer = max(answer, len(q))

print(answer)