from sys import stdin as s

s = open("input.txt", "rt")

n = int(s.readline())

""" 
문제

N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.

"""

# 반복문과 range() 함수를 사용한다.
# range(start, end) 함수는 start 와 end 사이의 숫자들을 연속적으로 리턴한다. -> result = list(range(1, 5))

for i in range(1, 10):
    result = n * i
    print(str(n) + " * " + str(i) + " = " + str(result))