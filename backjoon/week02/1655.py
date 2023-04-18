from sys import stdin as s
import heapq

s = open("input.txt", "rt")
""" 
문제

백준이는 동생에게 "가운데를 말해요" 게임을 가르쳐주고 있다. 
백준이가 정수를 하나씩 외칠때마다 동생은 지금까지 백준이가 말한 수 중에서 중간값을 말해야 한다. 
만약, 그동안 백준이가 외친 수의 개수가 짝수개라면 중간에 있는 두 수 중에서 작은 수를 말해야 한다.

예를 들어 백준이가 동생에게 1, 5, 2, 10, -99, 7, 5를 순서대로 외쳤다고 하면, 동생은 1, 1, 2, 2, 2, 2, 5를 차례대로 말해야 한다. 
백준이가 외치는 수가 주어졌을 때, 동생이 말해야 하는 수를 구하는 프로그램을 작성하시오.

첫째 줄에는 백준이가 외치는 정수의 개수 N이 주어진다. 
N은 1보다 크거나 같고, 100,000보다 작거나 같은 자연수이다. 
그 다음 N줄에 걸쳐서 백준이가 외치는 정수가 차례대로 주어진다. 
정수는 -10,000보다 크거나 같고, 10,000보다 작거나 같다.

한 줄에 하나씩 N줄에 걸쳐 백준이의 동생이 말해야 하는 수를 순서대로 출력한다.
"""
n = int(s.readline().rstrip())
numbers = [int(a) for a in s.readlines()]
# 중간값보다 작은 수가 들어감 최대힙 구현
leftheap = []
# 중간값보다 큰 수가 들어감 최소힙 구현
rightheap = []

for i in range(n):
    num = numbers[i]

    # leftheap의 길이가 rightheap의 길이와 같다면
    if len(leftheap) == len(rightheap):
        # leftheap에 현재 숫자를 음수 형태로 삽입 (최대힙 구현)
        heapq.heappush(leftheap, (-num, num))
    
    # 길이가 다르다면
    else:
        # rightheap에 현재 숫자를 삽입
        heapq.heappush(rightheap, (num))

    # 양쪽 heap에 요소들이 존재한다면, 
    # leftheap의 루트에 음수를 곱한 값이 rightheap의 루트보다 크다면?
    if (len(leftheap) >= 1 and len(rightheap) >= 1 and leftheap[0][1] > rightheap[0]):
        # leftheap의 루트를 제거하고, 
        leftroot = heapq.heappop(leftheap)
        # leftheap의 루트에 음수를 곱한 값을 rightheap에 삽입
        heapq.heappush(rightheap, leftroot[0][1])

        # rightheap의 루트를 제거하고, 
        rightroot = heapq.heappop(rightheap)
        # rightheap의 루트에 음수를 곱한 값을 leftheap에 삽입
        heapq.heappush(leftheap, (-rightroot, rightroot))

    # leftheap의 루트에 음수를 곱한 뒤 출력
    print(leftheap[0][1])
