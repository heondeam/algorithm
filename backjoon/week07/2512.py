from sys import stdin as s

s = open("input.txt", "rt")
""" 2512. 예산 """



def find_answer():
    global costs, m

    maxValue = 0

    lt = 1
    rt = m

    while lt <= rt:
        mid = (lt + rt) // 2

        ans = []

        for cost in costs:
            if cost <= mid:
                ans.append(cost)
            else:
                ans.append(mid)

        maxValue = sum(ans)

        if maxValue > m:
            rt = mid - 1
        elif maxValue == m:
            return mid
        else:
            lt = mid + 1

    return rt

if __name__ == "__main__":
    # 지방의 수 3 <= n <= 10000
    n = int(s.readline().rstrip()) 
    # 각 지방 별 요청 예산
    costs = list(map(int, s.readline().rstrip().split()))
    # 총 예산
    m = int(s.readline().rstrip())



    # 배정된 예산들 중 최댓값인 정수를 출력한다.

    if sum(costs) <= m:
        # 모든 요청 배정 가능한 경우
        print(max(costs))
    else:
        print(find_answer())
