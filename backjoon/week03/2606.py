from sys import stdin as s

s = open("input.txt", "rt")
""" 
문제

신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다.
한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.
예를 들어 7대의 컴퓨터가 <그림 1>과 같이 네트워크 상에서 연결되어 있다고 하자. 
1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스는 2번과 5번 컴퓨터를 거쳐 3번과 6번 컴퓨터까지 전파되어 2, 3, 5, 6 네 대의 컴퓨터는 웜 바이러스에 걸리게 된다. 
하지만 4번과 7번 컴퓨터는 1번 컴퓨터와 네트워크상에서 연결되어 있지 않기 때문에 영향을 받지 않는다.
어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 
컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 
1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.

첫째 줄에는 컴퓨터의 수가 주어진다. 
컴퓨터의 수는 100 이하이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다.
둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다. 
이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.

1번 컴퓨터가 웜 바이러스에 걸렸을 때, 
1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.
"""


def find_parent(x):
    if parent[x] != x:
        return find_parent(parent[x])
    return parent[x]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    # 작은 루트 노드를 기준으로 합친다.
    if a < b:
        parent[b] = a
    else:
        parent[a] = b



if __name__ == "__main__":
    input_data = [list(map(int, s.rstrip().split())) for s in s.readlines()]
    v, e, graph = input_data[0][0], input_data[1][0], input_data[2:]

    parent = [0] * (v + 1)

    cnt = 0

    # 부모 테이블 초기 세팅 (자기 자신을 루트로)
    for i in range(1, v + 1):
        parent[i] = i

    for i in range(e):
        a, b = graph[i][0], graph[i][1]
        union(a, b)

    for i in range(1, v + 1):
        # 루트 노드가 1인 노드들 즉, 같은 집합에 속한 노드들의 개수를 센다.
        if find_parent(i) == 1:
            cnt += 1

    print(cnt - 1)