from sys import stdin as s

s = open("input.txt", "rt")

""" 

문제

문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 
즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. 
S에는 QR Code "alphanumeric" 문자만 들어있다.

QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.

첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 
각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다. 
S의 길이는 적어도 1이며, 20글자를 넘지 않는다. 

"""

input_list = [str(a.rstrip()) for a in s.readlines()]

case_num = int(input_list[0])

del input_list[0]

for i in range(case_num):
    loop_num, text = map(str, input_list[i].split(" "))
    splited_text = [str(a) for a in text]
    output = ""

    for j in range(len(splited_text)):

        for k in range(int(loop_num)):
            output += splited_text[j]

    print(output)
