from sys import stdin as s

s = open("input.txt", "rt")
""" 1912. 연속합 """

# 임의의 수열에서 몇 개를 뽑아서 구할 수 있는 합 중 가장 큰 합을 구하자.

if __name__ == "__main__":
    n = int(s.readline().rstrip())
    numbers = list(map(int, s.readline().rstrip().split()))

    for i in range(1, n):
        numbers[i] = max(numbers[i], numbers[i] + numbers[i-1])

    print(max(numbers))