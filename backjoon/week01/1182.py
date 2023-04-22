from sys import stdin as s

s = open("input.txt", "rt")

""" 
문제

N개의 정수로 이루어진 수열이 있을 때, 
크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하시오.

첫째 줄에 정수의 개수를 나타내는 N과 정수 S가 주어진다. 
(1 ≤ N ≤ 20, |S| ≤ 1,000,000) 둘째 줄에 N개의 정수가 빈 칸을 사이에 두고 주어진다. 
주어지는 정수의 절댓값은 100,000을 넘지 않는다.

부분수열이란 해당 수열에 있는 수들의 모든 조합을 말합니다.
예를 들면, 아래 수열의 경우
[1, 2, 1, 3, 5, 6]
[2, 1, 3] 처럼 수들이 연속된 경우 뿐만 아니라,
[1, 1, 3] 처럼 불연속적으로 선택된 수들도 부분 수열입니다. 다만 아무 것도 선택하지 않는 경우([ ])는 제외됩니다.

첫째 줄에 합이 S가 되는 부분수열의 개수를 출력한다.
"""
def find_answer(L, arr):
    global ans, cnt

    if L == N:
        if len(ans) > 0 and sum(ans) == S:
            cnt += 1

        return 
    else:
        ans.append(data[L])
        find_answer(L + 1, ans)
        ans.remove(data[L])
        find_answer(L + 1, ans)

if __name__ == "__main__":
    N, S = map(int, s.readline().split())
    data = list(map(int, s.readline().split()))
    ans = []
    cnt = 0

    find_answer(0, [])

    print(cnt)

