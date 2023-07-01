from sys import stdin as s

s = open("input.txt", "rt")

""" 
문제

한수는 크기가 2^2 * 2^2인 2차원 배열을 Z모양으로 탐색하려고 한다. 
예를 들어, 2*2배열을 왼쪽 위칸, 오른쪽 위칸, 왼쪽 아래칸, 오른쪽 아래칸 순서대로 방문하면 Z모양이다.
N > 1인 경우, 배열을 크기가 2N-1 * 2N-1로 4등분 한 후에 재귀적으로 순서대로 방문한다.
다음 예는 22 * 22 크기의 배열을 방문한 순서이다.
N이 주어졌을 때, r행 c열을 몇 번째로 방문하는지 출력하는 프로그램을 작성하시오.

첫째 줄에 정수 N, r, c가 주어진다.
r행 c열을 몇 번째로 방문했는지 출력한다.
"""

N, r, c = map(int, s.readline().split())

ans = 0
def z(n,x,y):
    """ 
    n: 변의 길이
    x: 현재 위치의 x축의 값
    y: 현재 위치의 y축의 값 
    """
    global ans

    if x == r and c == y :
        print(ans)
        exit(0)

    if n == 1:
        ans +=1
        return
    
    if not ( x <= r < n+x  and y <= c < n+y ):
        ans += n*n
        return
    
    z(n//2, x, y)
    z(n//2, x, y +  n//2)
    z(n//2, x +n//2, y)
    z(n//2, x + n//2, y + n//2)
    
z(2**N,0,0)