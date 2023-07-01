from sys import stdin as s

s = open("input.txt", "rt")
""" 2406. 안정적인 네트워크 """

# 네트워크 고장이 발생하는 두가지 경우
# 1. 직접 연결되어 있는 두 컴퓨터의 연결이 끊어지는 경우
# 2. 컴퓨터가 고장나는 경우 -> 고장 나지 않은 컴퓨터끼리 연결되어 있기를 원함.

# 네트워크 연결 상태를 입력 받아서
# 해당 네트워크가 안정적인 네트워크인지 판별
# 아닐 경우에는 최소 비용으로 안정적으로 만들어야 함.

# 첫째 줄에 최소 비용 X와 연결할 컴퓨터들의 쌍의 개수 K를 출력.
# 다음 k개의 줄에 두 정수로 연결할 컴퓨터들의 번호를 출력해라 
# 안정적일 경우 x = 0, y = 0이다.

""" 크루스칼 알고리즘 사용 최소 스패닝 트리 구성 확인 """
""" 2번 컴퓨터부터 n번 컴퓨터까지의 MST를 구성하자. """
def find_parent(x):
    global parent

    if parent[x] != x:
        return find_parent(parent[x])
    
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
    # 컴퓨터의 개수, 연결되어 있는 지사 컴퓨터들의 쌍의 개수
    n, m = list(map(int, s.readline().rstrip().split()))
    # 간선들
    edges = [list(map(int, s.readline().rstrip().split())) for _ in range(m)]
    # 비용들
    costs = [list(map(int, s.readline().rstrip().split())) for _ in range(n)]

    # sortedEdges
    sorted_edges = []

    parent = [0] * (n + 1)

    for i in range(1, n+1):
        parent[i] = i

    for edge in edges:
        x, y = edge
        union(x, y)

    for i in range(1, n):
        for j in range(1, n):
            sorted_edges.append((costs[i][j], i + 1, j + 1))

    sorted_edges.sort()

    x = 0
    k = 0
    res = []

    for edge in sorted_edges:
        cost, a, b = edge

        if find_parent(a) != find_parent(b):
            union(a, b)
            res.append((b, a))
            x += cost
            k += 1

    print(x, k)
    for i in range(len(res)):
        print(res[i][0], res[i][1])