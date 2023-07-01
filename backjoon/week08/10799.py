from sys import stdin as s

s = open("input.txt", "rt")
""" 10799. 쇠막대기 """


if __name__ == "__main__":
    pattern = s.readline().rstrip()
    nowSticks = 0
    totalSticks = 0
    stack = []

    for p in pattern:
        stack.append(p)

        if p == "(":
            nowSticks += 1

        elif p == ")":
            exP = stack[-2]

            if exP == "(":
                # 레이저 발싸
                nowSticks -= 1
                totalSticks += nowSticks
            elif exP == ")":
                # 쇠막대기 끝남
                nowSticks -= 1
                totalSticks += 1

    print(totalSticks)