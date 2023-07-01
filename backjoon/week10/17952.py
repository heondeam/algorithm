from sys import stdin as s

s = open("input.txt", "rt")
""" 17952. 과제는 끝나지 않아! """

# 과제를 진행하는 규칙
# 1. 과제는 가장 최근에 나온 순서대로 한다. 과제를 받으면 바로 시작.
# 2. 과제를 하던 도중 새로운 과제가 나온다면, 하던 과제를 중단하고 새로운 과제를 진행한다.
# 3. 새로운 과제가 끝났다면, 이전에 하던 과제를 이전에 하던 부분부터 이어서 한다. 
# (성애는 기억력이 좋기 때문에 아무리 긴 시간이 지나도 본인이 하던 부분을 기억할 수 있다.)

# 예상 과제 점수를 구하자

if __name__ == "__main__":
    # 이번 학기는 총 n분이다.
    n = int(s.readline().rstrip())
    # 1 A T  과제의 만점은 A점, 이 과제를 해결하는데 T분
    # 0      해당 시점에는 과제가 주어지지 않음
    tasks = [list(map(int, s.readline().rstrip().split())) for _ in range(n)]

    total = 0
    stack = []

    for i in range(n):
        exist_task = tasks[i][0]

        if exist_task:
            # 해당 분에 과제가 주어짐.

            if tasks[i][2] - 1 == 0:
                total += tasks[i][1]
            else:
                stack.append((tasks[i][1], tasks[i][2] - 1)) 

        else:
            # 해당 분에 과제가 주어지지 않음.
            # 이전 과제를 이어서 진행함.
            if stack:
                stack[-1] = (stack[-1][0], stack[-1][1] - 1)

                if stack[-1][1] == 0:
                    total += stack[-1][0]
                    stack.pop()

    print(total)