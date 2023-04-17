from sys import stdin as s

s = open("input.txt", "rt")
""" 
문제

KOI 부설 과학연구소에서는 많은 종류의 산성 용액과 알칼리성 용액을 보유하고 있다.
각 용액에는 그 용액의 특성을 나타내는 하나의 정수가 주어져있다. 
산성 용액의 특성값은 1부터 1,000,000,000까지의 양의 정수로 나타내고, 
알칼리성 용액의 특성값은 -1부터 -1,000,000,000까지의 음의 정수로 나타낸다.

같은 양의 두 용액을 혼합한 용액의 특성값은 혼합에 사용된 각 용액의 특성값의 합으로 정의한다. 
이 연구소에서는 같은 양의 두 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들려고 한다.

예를 들어, 주어진 용액들의 특성값이 [-2, 4, -99, -1, 98]인 경우에는 특성값이 -99인 용액과 특성값이 98인 용액을 혼합하면 특성값이 -1인 용액을 만들 수 있고, 
이 용액이 특성값이 0에 가장 가까운 용액이다. 
참고로, 두 종류의 알칼리성 용액만으로나 혹은 두 종류의 산성 용액만으로 특성값이 0에 가장 가까운 혼합 용액을 만드는 경우도 존재할 수 있다.

산성 용액과 알칼리성 용액의 특성값이 주어졌을 때, 이 중 두 개의 서로 다른 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들어내는 두 용액을 찾는 프로그램을 작성하시오.
"""
def binary_search():
    global datas

    start = 0
    end = len(datas) - 1
    ans = abs(datas[start] + datas[end])
    lt = 0
    rt = len(datas) - 1

    while start < end:
        if abs(datas[start] + datas[end]) <= ans:
            ans = abs(datas[start] + datas[end])

            lt = start
            rt = end

        if datas[start] + datas[end] < 0:
            start += 1
        else:
            end -= 1
    
    print(datas[lt], datas[rt])


if __name__ == "__main__":
    n = int(s.readline().rstrip())
    datas = list(map(int, s.readline().rstrip().split()))
    datas.sort()

    binary_search()