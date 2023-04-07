from sys import stdin as s

s = open("input.txt", "rt")

""" 

문제

주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

"""

# 소수의 정의 1과 자기 자신으로만 나누어 지는 수
# 특정 숫자 n이 존재할 때 2부터 n-1까지 숫자로 n을 나눴을 때 0 이 있다면 소수가 아니다.

input_list = [str(a).rstrip() for a in s.readlines()]

n = int(input_list[0])
arr = [int(a) for a in input_list[1].split()]

result = []

for i in range(n):
    if arr[i] != 1 :
        for j in range(2, arr[i]):
            if arr[i] % j == 0:
                result.append(arr[i])
                break
    else:
        result.append(1)


print(n - len(result))
