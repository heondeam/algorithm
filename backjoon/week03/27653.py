from sys import stdin as s

s = open("input.txt", "rt")
""" 
문제

정점이 
N개인 트리가 주어진다. 정점에는 1부터 N까지 번호가 붙어있다. 
각 정점에는 가중치가 존재하는데, 초기에 모든 가중치는 0이다.

당신은 다음 연산을 트리에 반복하여 
1 이상 N 이하의 모든 i에 대해 
정점 i의 가중치가 A_i가 되도록 만들고 싶다.

연산: 주어진 트리의 임의의 부분 연결 그래프에 대하여, 
그 그래프에 포함되는 정점의 가중치를 1씩 증가시킨다.
1 이상 N 이하의 모든 i에 대해 
정점 i의 가중치가 A_i가 되도록 하는 최소 연산 횟수를 구하라.
"""
def DFS(v) :
    """ v : 탐색을 시작할 정점 """

    # stack
    stack = [(v, 0)]
    visited[v] = 1

    while stack:
        
        



if __name__ == "__main__":
    input_data = [s.rstrip() for s in s.readlines()]
    n = int(input_data[0])
    A = [0] + list(map(int, input_data[1].split()))
    edges = [list(map(int, s.split() )) for s in input_data[2:]]

    graph = []

    visited = [0] * (n + 1)

    weights = [0] * (n + 1)

    for i in range(n + 1):
        graph.append([])

    for edge in edges:
        s, e = edge

        graph[s].append(e)
        graph[e].append(s)