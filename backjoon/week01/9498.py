from sys import stdin as s

s = open('input.txt', 'rt')

n = int(s.readline())

""" 
문제

시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

"""
def test_score(num):
    if num <= 100 and num >= 90:
        print("A")
    elif num < 90 and num >= 80:
        print("B")
    elif num < 80 and num >= 70:
        print("C")
    elif num < 70 and num >= 60:
        print("D")
    elif num < 60:
        print("F")
    

test_score(n)