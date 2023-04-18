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



def binary_search(num):
    """
        num : 찾는 값
    """
    global a

    start = 0
    end = len(a) - 1

    while start <= end:
        mid = (start + end) // 2

        if a[mid] == num:
            return True
        elif a[mid] < num:
            start = mid + 1
        elif a[mid] > num:
            end = mid - 1

if __name__ == "__main__":
    input_datas = [list(map(int, s.readline().rstrip().split())) for _ in range(4)]
    n, a, m, data = input_datas[0][0], input_datas[1], input_datas[2][0], input_datas[3]
    a.sort()

    for i in range(len(data)):
        if binary_search(data[i]):
            print(1)
        else:
            print(0)