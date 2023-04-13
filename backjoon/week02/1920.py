from sys import stdin as s

s = open("input.txt", "rt")

""" 
문제

N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 
다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 
다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 
모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.
M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.
"""

def binary_search(n):
    global A

    # 좌측 포인터 (인덱스)
    lt = 0
    # 우측 포인터 (인덱스)
    rt = len(A) - 1

    while lt <= rt:
        # 중간값의 인덱스
        mid = (lt+rt) // 2

        if A[mid] == n:
            print(1)
            break
        
        if n < A[mid]:
            rt = mid - 1
        elif n > A[mid]:
            lt = mid + 1

    else: 
        print(0)


if __name__ == "__main__":
    input_data = [a.rstrip().split() for a in s.readlines()]

    N, M = int(input_data[0][0]), int(input_data[2][0])

    A = list(map(int, input_data[1]))
    nums = list(map(int, input_data[3]))

    A.sort()

    for i in range(M):
        binary_search(nums[i])