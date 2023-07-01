""" 
변수명 정하기 
    1) 영문과 숫자, _로 구성된다.
    2) 대소문자 구분
    3) 문자나, _로 시작한다.
    4) 특수문자 불가
    5) 키워드 사용 불가
"""

# a = 1
# print(a)

#값 교환
# a, b = 10, 20
# print(a, b)
# a, b = b, a
# print(a, b)

#변수 타입
# a = 12345 # 정수 타입 int
# print(type(a))
# a = 12.123456789 # 실수 타입 float, 8byte 까지만 허용된다.
# print(type(a))
# a = 'student' # 문자 타입 str
# print(type(a))

# 출력 방식
# print("number")
# a, b, c = 1, 2, 3
# print(a, b, c)
# print("number", a, b, c)
# print(a, b, c, sep=', ')
# print(a, b, c, sep=',')
# print(a, b, c, sep='')
# print(a, b, c, sep='\n')
# print(a) # 기본적으로 줄바꿈 된다.
# print(a, end=' ') # 줄바꿈 하지 않는다.
# print(b, end=' ')
# print(c)

"""  
변수 입력과 연산자
"""

# a = input("숫자를 입력하세요")
# print(a)

# a, b = input("숫자를 입력하세요: ").split()
# print(type(a))
# c = a + b # 문자 간의 + 연산자는 a + b = ab
# print(type(c))
# print(c)

# a = int(a)
# b = int(b)
# print(type(a))
# print(type(b))

# a, b = map(int, input("숫자를 입력하세요 : ").split()) # map 함수 사용법
# print(a + b) # 더하기
# print(a - b) # 빼기
# print(a * b) # 곱하기
# print(a / b) # 나누기
# print(a // b) # 몫
# print(a % b) # 나머지
# print(a ** b) # 거듭제곱

# a = 4.3
# b = 5
# c = a + b 
# print(type(c), c) # 실수형과 정수형의 사칙연산 시 실수형으로 연산 결과가 출력된다.

""" 
조건문 if (분기, 중첩)
"""

# x = 7
# if x == 7:
#     print("lucky", end=" ") # 파이썬에서는 4칸 들여쓰기를 해야 해당 코드가 블럭에 종속됨
#     print("zz")

# if x != 7:
#     print("no lucky", end=" ")
#     print("ㅠㅠ")

# x = 14
# if x >= 10:
#     if x % 2 == 1: 
#         print("10이상의 홀수") # 중첩 조건문
#     else:
#         pass

# x = 10
# if x > 0:
#     if x <= 9:
#         print("10보다 작은 자연수")

# x = 7
# if x > 0 and x < 10: # 논리 연산자 and 즉, 교집합을 의미함.
#     print("10보다 작은 자연수")

# x = 7
# if 0 < x < 10:
#     print("10보다 작은 자연수")

# x = 10
# if x > 0:
#     print("양수")
# else:
#     print("음수")

# x = 33

# if x >= 90:
#     print("A")
# elif x >= 80:
#     print("B")
# elif x >= 70:
#     print("C")
# elif x >= 60:
#     print("D")
# else:
#     print("F")

""" 
반복문 (for, while)
"""

# a = range(1, 10) # a부터 b미만까지 정수 리스트를 만듬. a가 없을 경우 0부터
# print(list(a))

# for i in range(1, 11):
#     print(i)

# for i in range(10, 0, -1): 
#     print(i)

# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# while True: # 무한 반복문
#     print(i)
#     i += 1
#     if i > 10:
#         break

# i = 10

# while i >= 1:
#     print(i)
#     i -= 1

# for i in range(1, 11):
#     if i % 2 == 0: # 짝수일 때
#         continue # 해당 조건에 합당한 i는 해당 루프가 종료됨

#     print(i)

# for i in range(1, 11):
#     print(i)

#     if i  > 15:
#         break # 조건이 참이면 반목문을 끝냄
# else:
#     # for문이 정상적으로 실행되고 난 후에 실행되는 코드
#     print(11)

""" 
반복문을 이용한 문제풀이
    1) 1부터 N까지 홀수 출력하기
    2) 1부터 N까지의 합 구하기
    3) N의 약수 출력하기
"""

# n = int(input("N을 입력해주세요. : "))

# for i in range(1, n + 1):
#     if i % 2 != 0:
#         print(i)


# sum = 0
# for i in range(1, n + 1):
#     sum += i

# print(sum)

# for i in range(1, n + 1):
#     if n % i == 0:
#         print(i, end=" ")

""" 
중첩 반복운 (2중 for문)
"""

# for i in range(5):
#     print('i:', i, sep="", end=" ")
#     for j in range(5):
#         print('j:', j, sep="", end = " ")
#     print()

# for i in range(5):
#     for j in range(5):
#         print("*", end= " ")
#     print()

# for i in range(5):
#     for j in range(i + 1):
#         print("*", end=" ")
#     print()

# for i in range(5, 0, -1):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# for i in range(5):
#     for j in range(5 - i):
#         print("*", end=" ")
#     print()

""" 
문자열과 내장함수
"""

# msg = "It is Time"

# print(msg.upper()) # 문자열의 모든 문자들을 대문자화, 원본 문자열은 변경되지 않음
# print(msg.lower()) # 문자열의 모든 문자들을 소문자화, 원본 문자열은 변경되지 않음

# tmp = msg.upper()
# print(tmp.find('T')) # 문자열에서 T를 찾아서 처음으로 발견된 T의 인덱스를 반환한다.
# print(tmp.count('T')) # 문자열에서 T의 개수를 반환한다.
# print(msg[:2]) # 문자열 slice 기능, 0 ~ 2번 index까지의 문자열을 반환한다.
# print(msg[3:5]) # 인덱스 3 ~ 4번 까지의 문자열을 반환한다.
# print(len(msg)) # len() 은 길이를 반환한다.

# for i in range(len(msg)):
    # print(msg[i], end= ' ')

# for x in msg: # 문자열 하나하나에 직접 접근한다 x는 원소
#     print(x, end = " ")

# for x in msg:
#     if x.isupper(): # x가 대문자면 참.
#         print(x)
#     elif x.islower(): # x가 소문자면 참.
#         print(x)

# for x in msg:
#     if x.isalpha(): # x가 알파벳이면 참.
#         print(x, end= "")
        

# tmp = "AZaz"
# for x in tmp:
    # print(ord(x)) # ord()는 x의 아스키 넘버를 반환한다.

# tmp = 65
# print(chr(tmp)) # chr()은 해당 아스키 넘버에 해당하는 문자를 반환한다.


""" 
리스트와 내장함수(1)
"""
# import random as r

# a = [] # 빈리스트 만들기
# b = list() # 빈리스트 만들기
# a = [1, 2, 3, 4, 5] # 1, 2, 3, 4, 5 라는 원소를 가지는 리스트 만들기
# b = list(range(1, 11)) # 1 ~ 10 을 원소로 가지는 리스트 만들기
# c = a + b # 리스트 함치기

# a.append(6) # 리스트 끝에 원소 추가하기
# a.insert(3, 7) # a의 3번 인덱스에 7이라는 원소가 들어감
# a.pop() # a의 끝의 원소가 제거된다.
# a.pop(3) # a의 3번 인덱스의 원소가 제거된다.
# a.remove(4) # a에서 4라는 값을 제거한다.
# a.index(5) # a에서 5의 인덱스 번호를 반환한다.

# a = list(range(1, 11))
# print(sum(a)) # a리스트의 모들 원소들의 합을 반환함.
# print(max(a)) # a리스트의 최댓값 찾아줌.
# print(min(a)) # a리스트의 최솟값 찾아줌.
# print(max(1, 5)) # 인자 값들 중에서 최대값을 찾아줌.
# print(min(1, 5)) # 인자 값들 중에서 최소값을 찾아줌.
# r.shuffle(a) # a의 값을 랜덤으로 섞는다.
# a.sort() # 리스트 a를 오름차순으로 정렬한다.
# a.sort(reverse=True) # 리스트 a를 내림차순으로 정렬한다.
# a.clear() # 리스트 내의 원소들을 모두 제거한다.

""" 
리스트와 내장함수(2)
"""

# a = [23, 12, 36, 53, 19]
# print(a[:3]) # 인덱스 0 ~ 2까지의 부분 리스트를 출력한다.
# print(a[1:4]) # 인덱스 1 ~ 3까지의 부분 리스트를 출력한다.
# print(len(a)) # 리스트의 길이를 반환한다.

# for i in range(len(a)):
#     print(a[i], end= " ")

# for x in a: # 리스트의 원소에 직접적으로 접근 
#     print(x, end= " ")

# for x in a:
#     if x % 2 != 0:
#         print(f'{x}는 홀수입니다.')

# for x in enumerate(a): # x가 튜플이라는 자료구조로 출력된다.  -> (index, x)
#     print(x)

# b = () # 빈 튜플 만들기
# b = (1, 2, 3, 4, 5) # 튜플 만들기
# b[0] = 7 # 튜블의 원소는 변경할 수 없다.

# for x in enumerate(a):
    # print(x[0], x[1])
    
# for index, value in enumerate(a): # 인덱스와 그 인덱스의 원소에 동시에 접근하기 위함.
#     print(index, value)

# if all(50 > x for x in a): # all 함수는 조건이 모두 참이면 참을 반환한다.
#     print("모두 작다.")
# else:
#     print("거짓")

# if any(11 > x for x in a): # any 함수는 조건 중 하나라도 참이면 참을 반환한다.
#     print("모두 작다.")
# else:
#     print("모두 거짓")

""" 
2차원 리스트 생성과 접근
"""

# a = [0] * 3 # 크기가 3인 1차원 리스트 만들기 
# print(a)

# a = [[0] * 3 for _ in range(3)] # 2차원 리스트 만들기
# print(a) 

# 2차원 리스트는 행렬로 접근하는 편이 좋다 (표)
# for x in a: 
#     print(x)

# for x in a:
#     for y in x:
#         print(y, end = " ")
#     print()


""" 
함수 만들기
"""

# def add(a, b):
#     c = a + b
#     d = a -1

#     return c, d # 튜플 자료 구조로 리턴

# print(add(4, 5))


# def isPrime(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
    

# a = [12, 13, 7, 9, 19]

# for x in a:
#     if isPrime(x):
#         print(x)

""" 
람다 함수 (익명 함수) == 람다 표현식
"""

# # def plus_one(x):
#     return x + 1


# plus_two = lambda x: x + 12 # 람다 표현식
# print(plus_two(1))

""" 
람다 함수는 내장함수의 
"""

# a = [1, 2, 3]

# print(list(map(plus_one, a))) # map 함수의 첫번째 인자는 함수
# print(list(map(lambda x: x + 12, a))) # map 함수의 첫번째 인자는 함수