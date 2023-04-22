from sys import stdin as s
import heapq

s = open("input.txt", "rt")
""" 
문제

그래프가 주어졌을 때, 그 그래프의 최소 스패닝 트리를 구하는 프로그램을 작성하시오.
최소 스패닝 트리는, 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리를 말한다.

첫째 줄에 정점의 개수 V(1 ≤ V ≤ 10,000)와 간선의 개수 E(1 ≤ E ≤ 100,000)가 주어진다. 
다음 E개의 줄에는 각 간선에 대한 정보를 나타내는 세 정수 A, B, C가 주어진다. 
이는 A번 정점과 B번 정점이 가중치 C인 간선으로 연결되어 있다는 의미이다. C는 음수일 수도 있으며, 절댓값이 1,000,000을 넘지 않는다.

그래프의 정점은 1번부터 V번까지 번호가 매겨져 있고, 임의의 두 정점 사이에 경로가 있다.
최소 스패닝 트리의 가중치가 -2,147,483,648보다 크거나 같고, 2,147,483,647보다 작거나 같은 데이터만 입력으로 주어진다.

첫째 줄에 최소 스패닝 트리의 가중치를 출력한다.
"""

# Kruskal's Algorithm
"""
def find_parent(x):
    global parent

    if parent[x] != x:
        parent[x] = find_parent(parent[x])

    return parent[x]

def union(a, b):
    global parent

    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


if __name__ == "__main__":
    v, e = list(map(int, s.readline().rstrip().split()))
    edges = []
    parent = [0] * (v + 1)
    result = 0

    for i in range(1, v + 1):
        parent[i] = i

    for _ in range(e):
        a, b, cost = list(map(int, s.readline().rstrip().split()))

        edges.append((cost, a, b))

    edges.sort()

    for edge in edges:
        cost, a, b = edge

        if find_parent(a) != find_parent(b):
            union(a, b)
            result += cost

    print(result)
"""
# Prim Algorithm
def prim(start, weight):
    global v, graph

    visit = [0] * (v + 1) # 방문한 정점을 처리하기 위한 배열
    q = [[weight, start]] # 힙 구조를 사용하기 위해 가중치를 앞에 둠.
    ans = 0 # 가중치의 합
    cnt = 0 # 간선의 개수

    while cnt < v: # 트리에서 간선의 개수는 노드가 n 개일 때 n -1 개이다.
        k, v = heapq.heappop(q)
        if visit[v]: continue # 방문한 정점이면 지나감
        visit[v] = 1 # 방문을 안했으면 방문 처리함
        ans += k  # 해당 정점까지의 가중치를 더해줌
        cnt += 1  # 간선의 갯수를 더해준다.

        # 해당 정점의 간선 정보를 불러온다.
        for u, w in graph[v]:
            # 힙에 push 해준다.
            heapq.heappush(q, [w, u])
    return ans

if __name__ == "__main__":
    v, e = list(map(int, s.readline().rstrip().split()))
    graph = [[] for _ in range(v + 1)]

    for _ in range(e):
        u, v, w = map(int, s.readline().rstrip().split())

        graph[u].append([v, w])
        graph[v].append([u, w])

