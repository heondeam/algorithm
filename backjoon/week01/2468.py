from sys import stdin as s

s = open("input.txt", "rt")

""" 
문제

첫째 줄에는 어떤 지역을 나타내는 2차원 배열의 행과 열의 개수를 나타내는 수 N이 입력된다. (N은 2 이상 100 이하의 정수이다.)
둘째 줄부터 N개의 각 줄에는 2차원 배열의 첫 번째 행부터 N번째 행까지 순서대로 한 행씩 높이 정보가 입력된다.
각 줄에는 각 행의 첫 번째 열부터 N번째 열까지 N개의 높이 정보를 나타내는 자연수가 빈 칸을 사이에 두고 입력된다. (높이는 1이상 100 이하의 정수이다.)

첫째 줄에 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수를 출력한다.
"""

N = int(s.readline())

maps = [list(map(int, s.readline().split())) for _ in range(N)]

for r in maps:
    for region in r:
        print(region)