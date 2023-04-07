from sys import stdin as s

s = open("input.txt", "rt")

""" 

문제

영어 대소문자와 공백으로 이루어진 문자열이 주어진다. 
이 문자열에는 몇 개의 단어가 있을까? 이를 구하는 프로그램을 작성하시오. 
단, 한 단어가 여러 번 등장하면 등장한 횟수만큼 모두 세어야 한다.

"""

# split()과 split(" ")의 차이에 대해서 이해
# split()은 공백이 1개이건 2개이건 n개이건 상관없이 무조건 1개로 보고 처리
# split(" ")은 공백 1개, 1개를 각각의 공백으로 따로 따로 처리

input_text = s.readline().strip().split()

print(len(input_text))