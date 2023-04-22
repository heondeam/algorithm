from sys import stdin as s

s = open("input.txt", "rt")
""" 
문제

방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 
둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

첫째 줄에 연결 요소의 개수를 출력한다.
"""
# class Node:
#     def __init__(self, key, parent) -> None:
#         self.key = key
#         self.parent = parent if parent else self
#         self.rank = 0

# def makeSet(n, p):
#     return Node(n, p)

# 특정 원소가 속한 집합을 찾는다.
def find_parent(x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출 (path compression)
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합친다. (union)
def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    # 작은 루트 노드를 기준으로 합침
    if a < b :
        parent[b] = a
    else:
        parent[a] = b

if __name__ == "__main__":
    n, m = list(map(int, s.readline().rstrip().split()))
    tmp = 0
    cnt = 0

    # 부모 테이블 초기화
    parent = [0] * (n + 1)

    # 부모 테이블상의, 각 노드의 부모를 자기 자신으로 초기화
    for i in range(1, n + 1):
        parent[i] = i

    # Union 연산을 수행
    for i in range(m):
        a, b = map(int, s.readline().rstrip().split())
        union(a, b)

    for i in range(1, n + 1):
        if find_parent(i) != tmp:
            tmp = find_parent(i)
            cnt += 1

    print(cnt)