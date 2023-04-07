from sys import stdin as s

s = open('input.txt', 'rt')

""" 
문제 

세 자리 수) * (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.

(1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.

"""

a, b = map(int, s.readlines())

b_array = [int(a) for a in str(b)]

print(a * b_array[2]) # (3) 출력
print(a * b_array[1]) # (4) 출력
print(a * b_array[0]) # (5) 출력
print(a * b) # (6) 출력