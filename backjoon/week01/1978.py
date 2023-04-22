from sys import stdin as s
import math

s = open("input.txt", "rt")

""" 

문제

주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

"""

# 소수의 정의 1과 자기 자신으로만 나누어 지는 수
# 특정 숫자 n이 존재할 때 2부터 n-1까지 숫자로 n을 나눴을 때 0 이 있다면 소수가 아니다.

n = int(s.readline())
data = list(map(int, s.readlines()[0].split()))

print(data)

def isPrime(x):
    if x == 1:
        return False

    for i in range(2, int(math.sqrt(x) + 1)):
            if x % i == 0:
                    return False

    return True
    
cnt = 0
for i in range(n):
    if isPrime(data[i]):
        cnt += 1
else:
    print(cnt)