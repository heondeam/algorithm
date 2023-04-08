from sys import stdin as s

s = open("input.txt", "rt")

""" 
문제

알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.
1. 길이가 짧은 것부터
2. 길이가 같으면 사전 순으로
3. 단, 중복된 단어는 하나만 남기고 제거해야 한다.
"""

n = int(s.readline())
arr = [str(a).rstrip() for a in list(s.readlines())]


# 중복 제거
set_list = set(arr)
# 리스트 자료구조로 다시 변환
re_arr = list(set_list)
# 문자 알파벳 순 정렬
re_arr.sort()
# 문자 길이 순 정렬
re_arr.sort(key = len)

for a in re_arr:
    print(a)