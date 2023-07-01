from sys import stdin as s

s = open("input.txt", "rt")

""" 
문제

원 영역

x축 위에 원이 N개 있다. 원은 서로 교차하지 않는다. 하지만, 접할 수는 있다.
원으로 만들어지는 영역이 몇 개인지 구하는 프로그램을 작성하시오.
영역은 점의 집합으로 모든 두 점은 원을 교차하지 않는 연속되는 곡선으로 연결될 수 있어야 한다.

첫째 줄에 원의 개수 N(1 ≤ N ≤ 300,000)이 주어진다.
다음 N개 줄에는 각 원의 정보 xi와 ri가 정수로 주어진다. xi는 원의 중심 좌표이며, ri는 반지름이다. (-109 ≤ xi ≤ 109, 1 ≤ ri ≤ 109)
입력으로 주어지는 원은 항상 유일하다.

첫째 줄에 원으로 인해서 만들어지는 영역의 개수를 출력한다.

"""
n = int(s.readline())
circles = []

# 원의 시작좌표와 끝좌표를 각각 ( 와 )로 나누어 저장한다.
for i in range(n):
    x, r = map(int, s.readline().split())
    circles.append((x-r, '('))
    circles.append((x+r, ')'))

# 좌표를 기준으로 오름 차순으로 정렬한다. 이 떄 좌표가 같으면 ')' 모양이 먼저 오게 정렬한다.
circles = sorted(circles, key=lambda x:(x[0], -ord(x[1])))

print(circles)

# 스택에는 좌표, 괄호 모양, 상태값이 들어간다.
stack = []
answer = 1

# 원을 괄호를 기준으로 나누면 원 1개당 괄호 2개가 나옴.
for i in range(n*2):
    position, bracket = circles[i]

    if len(stack) == 0:
        stack.append({"position": position, "bracket": bracket, "status": 0})
        continue

    # status 0: 기본값
    # status 1: 원 안의 원이 접해있음
    # 괄호가 닫히면 status 값을 확인한다 0일 때 +1 1일 때 +2
    if bracket == ')':
        if stack[-1]['status'] == 0:
            answer += 1
        elif stack[-1]['status'] == 1:
            answer += 2
        stack.pop()

        # 원이 인접해있는지 확인
        if i != n*2-1:
            if circles[i+1][0] != position:
                stack[-1]['status'] = 0
    else:
        if stack[-1]['pos'] == position:
            # 좌표값이 같으면 원이 접해있는 상태이다.
            stack[-1]['status'] = 1
            stack.append({'pos': position, 'bracket': bracket, 'status': 0})
        else:
            # 좌표값이 같지 않으면 원이 접해있지 않은 상태
            stack.append({"pos": position, "bracket": bracket, "status": 0})

print(answer)