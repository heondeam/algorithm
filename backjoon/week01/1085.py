from sys import stdin as s

s = open("input.txt", "rt")

input_text = s.readline().split()

x,y,w,h = map(int, input_text)


""" 

문제

한수는 지금 (x, y)에 있다. 직사각형은 각 변이 좌표축에 평행하고, 왼쪽 아래 꼭짓점은 (0, 0), 오른쪽 위 꼭짓점은 (w, h)에 있다. 
직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램을 작성하시오.

"""

# 현재 위치 x, y, 오른쪽 위 꼭지점의 위치 w, h
# 직사각형의 각 변으로 향하는 거리중 가장 짧은 거리를 구한다.
# 현수는 현재 x, y에 위치하고 있고 각 변으로 가는 거리는 x, y, h-y, w-x 가 되며 이중 최솟값이 정답이다.

print(min(x, y, h-y, w-x))