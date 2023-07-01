from sys import stdin as s
from collections import deque

s = open("input.txt", "rt")
""" 
문제

N명의 학생들을 키 순서대로 줄을 세우려고 한다. 
각 학생의 키를 직접 재서 정렬하면 간단하겠지만, 
마땅한 방법이 없어서 두 학생의 키를 비교하는 방법을 사용하기로 하였다. 
그나마도 모든 학생들을 다 비교해 본 것이 아니고, 
일부 학생들의 키만을 비교해 보았다.

일부 학생들의 키를 비교한 결과가 주어졌을 때, 
줄을 세우는 프로그램을 작성하시오.

첫째 줄에 N(1 ≤ N ≤ 32,000), M(1 ≤ M ≤ 100,000)이 주어진다. 
M은 키를 비교한 회수이다. 
다음 M개의 줄에는 키를 비교한 두 학생의 번호 A, B가 주어진다. 
이는 학생 A가 학생 B의 앞에 서야 한다는 의미이다.

학생들의 번호는 1번부터 N번이다.

첫째 줄에 학생들을 앞에서부터 줄을 세운 결과를 출력한다. 
답이 여러 가지인 경우에는 아무거나 출력한다.
"""

def topology_sort():
    # 큐 선언
    queue = deque()
    result = []

    # 진입 차수가 0인 노드를 큐에 넣는다.
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)

    # 큐가 빌 떄까지 반복한다.
    while queue:    
        # 큐에서 원소를 꺼낸다.
        nowVertext = queue.popleft()
        # 큐에서 빠져나간 노드를 순서대로 출력하면 위상정렬의 수행 결과를 알 수 있다.
        result.append(nowVertext)

        # 현재 노드와 인접한 노드들에 대해 간선을 제거한다. (진입 차수를 1씩 빼줌)
        for i in graph[nowVertext]:
            indegree[i] -= 1
            # 간선 제거 후 새롭게 진입 차수가 0이 되는 노드를 큐에 삽입한다.
            if indegree[i] == 0:
                queue.append(i)
    # 결과 출력
    print(*result)

if __name__ == "__main__":
    n, m = list(map(int, s.readline().rstrip().split()))
    edges = [list(map(int, s.readline().rstrip().split())) for _ in range(m)]

    graph = []

    # 진입 차수를 위한 리스트 초기화 (모두 0)
    indegree = [0] * (n + 1)
    
    for i in range(n + 1):
        graph.append([])

    for i in range(m):
        v, e = edges[i]
        # 정점 v에서 e로 이동 가능
        graph[v].append(e)
        # 진입 차수를 1 증가
        indegree[e] += 1

    topology_sort()