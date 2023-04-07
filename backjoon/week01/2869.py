from sys import stdin as s
import math

s = open("input.txt", "rt")

"""

문제

땅 위에 달팽이가 있다. 이 달팽이는 높이가 V미터인 나무 막대를 올라갈 것이다.
달팽이는 낮에 A미터 올라갈 수 있다. 하지만, 밤에 잠을 자는 동안 B미터 미끄러진다. 
또, 정상에 올라간 후에는 미끄러지지 않는다.
달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하는 프로그램을 작성하시오.

첫째 줄에 세 정수 A, B, V가 공백으로 구분되어서 주어진다. (1 ≤ B < A ≤ V ≤ 1,000,000,000)

첫째 줄에 달팽이가 나무 막대를 모두 올라가는데 며칠이 걸리는지 출력한다.

"""

# A = 올라갈 수 있는 거리 , B = 미끄러지는 거리 , V = 나무막대의 높이
# 올라가야 할 거리 = V - B
# 낮에만 올라갈 수 있으므로 하루에 갈 수 있는 거리 = A - B
input_list = [int(a) for a in s.readline().split()]

day_height = input_list[0]
night_height = input_list[1]
full_height = input_list[2]

# 올라갔다가, 내려간다는 것을 생각해야한다. 
print(math.ceil((full_height - night_height) / (day_height - night_height)))