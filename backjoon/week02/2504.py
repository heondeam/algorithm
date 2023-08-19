from sys import stdin as s

s = open("input.txt", "rt")
""" 
문제

4개의 기호 ‘(’, ‘)’, ‘[’, ‘]’를 이용해서 만들어지는 괄호열 중에서 올바른 괄호열이란 다음과 같이 정의된다.

한 쌍의 괄호로만 이루어진 ‘()’와 ‘[]’는 올바른 괄호열이다.
만일 X가 올바른 괄호열이면 ‘(X)’이나 ‘[X]’도 모두 올바른 괄호열이 된다.
X와 Y 모두 올바른 괄호열이라면 이들을 결합한 XY도 올바른 괄호열이 된다.
예를 들어 ‘(()[[]])’나 ‘(())[][]’ 는 올바른 괄호열이지만 ‘([)]’ 나 ‘(()()[]’ 은 모두 올바른 괄호열이 아니다. 
우리는 어떤 올바른 괄호열 X에 대하여 그 괄호열의 값(괄호값)을 아래와 같이 정의하고 값(X)로 표시한다.

‘()’ 인 괄호열의 값은 2이다.
‘[]’ 인 괄호열의 값은 3이다.
‘(X)’ 의 괄호값은 2×값(X) 으로 계산된다.
‘[X]’ 의 괄호값은 3×값(X) 으로 계산된다.
올바른 괄호열 X와 Y가 결합된 XY의 괄호값은 값(XY)= 값(X)+값(Y) 로 계산된다.
예를 들어 ‘(()[[]])([])’ 의 괄호값을 구해보자. ‘()[[]]’ 의 괄호값이 2 + 3×3=11 이므로 ‘(()[[]])’의 괄호값은 2×11=22 이다. 
그리고 ‘([])’의 값은 2×3=6 이므로 전체 괄호열의 값은 22 + 6 = 28 이다.

여러분이 풀어야 할 문제는 주어진 괄호열을 읽고 그 괄호값을 앞에서 정의한대로 계산하여 출력하는 것이다.

첫째 줄에 괄호열을 나타내는 문자열(스트링)이 주어진다. 단 그 길이는 1 이상, 30 이하이다.

첫째 줄에 그 괄호열의 값을 나타내는 정수를 출력한다. 만일 입력이 올바르지 못한 괄호열이면 반드시 0을 출력해야 한다.
"""
brackets = s.readline().rstrip()
stack = []
ans = 0
sum = 1

for i in range(len(brackets)):
    bracket = brackets[i]

    if bracket == "(":
        stack.append(bracket)
        sum *= 2
    elif bracket == "[":
        stack.append(bracket)
        sum *= 3    
    # 닫힌 괄호들은 이전 괄호들과 비교한다.
    elif bracket == ")":
        # 스택이 비었거나 이전 괄호 모양이 다르다면
        if not stack or stack[-1] == "[":
            ans = 0
            break
        # 쌍을 이루는 괄호일 경우
        elif brackets[i-1] == "(":
            ans += sum   
        # temp 초기화
        sum //= 2
        stack.pop()
    elif bracket == "]":
        # stack이 비어있거나 직전 괄호 모양이 다르면
        if not stack or stack[-1] == '(':
            ans = 0
            break
        elif brackets[i-1] == '[':
            ans += sum
        # temp 초기화
        sum //= 3
        stack.pop()

if stack:
    ans = 0

print(ans)