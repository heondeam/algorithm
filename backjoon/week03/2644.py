from sys import stdin as s
from collections import deque

s = open("input.txt", "rt")
""" 
문제

우리 나라는 가족 혹은 친척들 사이의 관계를 촌수라는 단위로 표현하는 독특한 문화를 가지고 있다. 
이러한 촌수는 다음과 같은 방식으로 계산된다. 
기본적으로 부모와 자식 사이를 1촌으로 정의하고 이로부터 사람들 간의 촌수를 계산한다. 
예를 들면 나와 아버지, 아버지와 할아버지는 각각 1촌으로 나와 할아버지는 2촌이 되고, 
아버지 형제들과 할아버지는 1촌, 나와 아버지 형제들과는 3촌이 된다.

여러 사람들에 대한 부모 자식들 간의 관계가 주어졌을 때, 
주어진 두 사람의 촌수를 계산하는 프로그램을 작성하시오.

사람들은 1, 2, 3, …, n (1 ≤ n ≤ 100)의 연속된 번호로 각각 표시된다. 
입력 파일의 첫째 줄에는 전체 사람의 수 n이 주어지고, 
둘째 줄에는 촌수를 계산해야 하는 서로 다른 두 사람의 번호가 주어진다. 
그리고 셋째 줄에는 부모 자식들 간의 관계의 개수 m이 주어진다. 
넷째 줄부터는 부모 자식간의 관계를 나타내는 두 번호 x,y가 각 줄에 나온다. 
이때 앞에 나오는 번호 x는 뒤에 나오는 정수 y의 부모 번호를 나타낸다.

각 사람의 부모는 최대 한 명만 주어진다.

입력에서 요구한 두 사람의 촌수를 나타내는 정수를 출력한다. 
어떤 경우에는 두 사람의 친척 관계가 전혀 없어 촌수를 계산할 수 없을 때가 있다. 
이때에는 -1을 출력해야 한다.
"""

def BFS(v, diff) :
    # v: 탐색을 시작할 노드 

    # 큐 생성 및 첫 노드와 레벨 푸쉬
    queue = deque([(v, 0)])
    # 방문 처리
    visited[v] = 1

    while queue:
        nowVertex = deque.popleft(queue)

        levels[nowVertex[0]] = (nowVertex[1], diff)

        # 방문하지 않은 인접한 노드들 방문
        for i in graph[nowVertex[0]]:
            if visited[i] != 1:
                queue.append((i, nowVertex[1] + 1))
                visited[i] = 1

if __name__ == "__main__":
    input_data = [s.rstrip() for s in s.readlines()]

    n = int(input_data[0])
    s, e = list(map(int, input_data[1].split()))
    m = int(input_data[2])
    edges = [list(map(int, s.split())) for s in input_data[3:]]

    graph = []

    visited = [0] * (n + 1)
    levels = [(0, 0)] * (n + 1)

    for i in range(n + 1):
        graph.append([])

    for edge in edges:
        v, u = edge

        graph[v].append(u)
        graph[u].append(v)

    BFS(1, 1)

    for i in range(len(levels)):
        if i != 1 and levels[i][0] == 0:
            BFS(i, i)

    
    if levels[s][1] == levels[e][1]:
        print(levels[s][0] + levels[e][0])
    else:
        print(-1)
