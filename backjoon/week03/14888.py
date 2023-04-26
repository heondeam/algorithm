from sys import stdin as s

s = open("input.txt", "rt")
""" 
문제

N개의 수로 이루어진 수열 A1, A2, ..., AN이 주어진다. 
또, 수와 수 사이에 끼워넣을 수 있는 N-1개의 연산자가 주어진다. 
연산자는 덧셈(+), 뺄셈(-), 곱셈(×), 나눗셈(÷)으로만 이루어져 있다.

우리는 수와 수 사이에 연산자를 하나씩 넣어서, 수식을 하나 만들 수 있다. 
이때, 주어진 수의 순서를 바꾸면 안 된다.

예를 들어, 6개의 수로 이루어진 수열이 1, 2, 3, 4, 5, 6이고, 
주어진 연산자가 덧셈(+) 2개, 뺄셈(-) 1개, 곱셈(×) 1개, 나눗셈(÷) 1개인 경우에는 총 60가지의 식을 만들 수 있다. 
예를 들어, 아래와 같은 식을 만들 수 있다.

1+2+3-4×5÷6
1÷2+3+4-5×6
1+2÷3×4-5+6
1÷2×3-4+5+6
식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행해야 한다. 
또, 나눗셈은 정수 나눗셈으로 몫만 취한다. 
음수를 양수로 나눌 때는 C++14의 기준을 따른다. 
즉, 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다. 
이에 따라서, 위의 식 4개의 결과를 계산해보면 아래와 같다.

1+2+3-4×5÷6 = 1
1÷2+3+4-5×6 = 12
1+2÷3×4-5+6 = 5
1÷2×3-4+5+6 = 7
N개의 수와 N-1개의 연산자가 주어졌을 때, 
만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램을 작성하시오.

첫째 줄에 수의 개수 N(2 ≤ N ≤ 11)가 주어진다. 
둘째 줄에는 A1, A2, ..., AN이 주어진다. (1 ≤ Ai ≤ 100) 
셋째 줄에는 합이 N-1인 4개의 정수가 주어지는데, 
차례대로 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수이다. 

첫째 줄에 만들 수 있는 식의 결과의 최댓값을, 둘째 줄에는 최솟값을 출력한다. 
연산자를 어떻게 끼워넣어도 항상 -10억보다 크거나 같고, 10억보다 작거나 같은 결과가 나오는 입력만 주어진다. 
또한, 앞에서부터 계산했을 때, 중간에 계산되는 식의 결과도 항상 -10억보다 크거나 같고, 10억보다 작거나 같다.
"""

def DFS(index, sum):
    global A, operators

    if index == len(A) - 1 :
        ans.append(sum)
        return
    else:
        # 재귀적으로 DFS 탐색 시작
        # 덧셈, 뺄셈, 곱셈, 나눗셈 4가지 경우의 수. (operator 배열의 인덱스 순)
        for i in range(4):
            # 횟수가 남아있다면
            if operators[i] > 0:
                if i == 0:
                    operators[i] -= 1
                    DFS(index + 1, sum + (A[index + 1]))
                    operators[i] += 1
                elif i == 1:
                    operators[i] -= 1
                    DFS(index + 1, sum - (A[index + 1]))
                    operators[i] += 1
                elif i == 2:
                    operators[i] -= 1
                    DFS(index + 1, sum * (A[index + 1]))
                    operators[i] += 1
                elif i == 3:
                    operators[i] -= 1
                    if sum < 0 :
                        DFS(index + 1, -(abs(sum) // (A[index + 1])))
                        operators[i] += 1
                    else:
                        DFS(index + 1, sum // (A[index + 1]))
                        operators[i] += 1

if __name__ == "__main__":
    n = int(s.readline().rstrip())
    A = list(map(int, s.readline().rstrip().split()))
    operators = list(map(int, s.readline().rstrip().split()))

    ans = []

    DFS(0, A[0])

    print(max(ans), min(ans), sep="\n")