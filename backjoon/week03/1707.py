from sys import stdin as s

s = open("input.txt", "rt")
""" 
문제

그래프의 정점의 집합을 둘로 분할하여, 각
집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있을 때, 
그러한 그래프를 특별히 이분 그래프 (Bipartite Graph) 라 부른다.

그래프가 입력으로 주어졌을 때, 이 그래프가 이분 그래프인지 아닌지 판별하는 프로그램을 작성하시오.

입력은 여러 개의 테스트 케이스로 구성되어 있는데, 
첫째 줄에 테스트 케이스의 개수 K가 주어진다. 
각 테스트 케이스의 첫째 줄에는 그래프의 정점의 개수 V와 간선의 개수 E가 빈 칸을 사이에 두고 순서대로 주어진다. 
각 정점에는 1부터 V까지 차례로 번호가 붙어 있다. 
이어서 둘째 줄부터 E개의 줄에 걸쳐 간선에 대한 정보가 주어지는데, 
각 줄에 인접한 두 정점의 번호 u, v (u ≠ v)가 빈 칸을 사이에 두고 주어진다.

K개의 줄에 걸쳐 입력으로 주어진 그래프가 이분 그래프이면 YES, 아니면 NO를 순서대로 출력한다.
"""

def DFS(v):
	
	# 스택을 이용한 DFS 수행
	# 튜플 형식으로 현재 정점값과 정점의 색을 스택에 푸시
	# 미방문일 경우 0, 시작 정점 1 인접 정접 -1
	myStack = [(v, 1)] 
	color[v] = 1

	# 스택이 빌 때까지 루프 수행
	while myStack:
		nowVertex, nowColor = myStack.pop()

		# 현재 정점에 인접한 정점에 대해서 컬러 판별
		for i in graph[nowVertex]:
			if color[i] == 0:
				myStack.append((i, -nowColor))
				color[i] = -nowColor

			elif color[i] == nowColor:
				return False

	return True

if __name__ == "__main__":
    t = int(s.readline().rstrip())

    for _ in range(t):
        v, e = map(int, s.readline().rstrip().split())

        graph = [[] for _ in range(v + 1)]
        color = [0] * (v + 1)

        for _ in range(e):
            u, v = map(int, s.readline().rstrip().split())

            graph[u].append(v)
            graph[v].append(u)

        for i in range(1, v + 1):
            if color[i] == 0:
                if not DFS(i):
                    print("NO")
                    break
        else:
            print("YES")
