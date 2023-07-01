from sys import stdin as s

s = open("input.txt", "rt")
""" 5397. 키로거 """


""" 시간초과 코드. list 삭제, 삽입 연산 때문에 시간 초과 나는 것 같다. """
if __name__ == "__main__":
    t = int(s.readline().rstrip())

    for _ in range(t):
        strings = [i for i in s.readline().rstrip()]

        strings.reverse()

        ans = []

        ptr = 0

        for _ in range(len(strings)):
            nowStr = strings.pop()
            l = len(ans)
            
            if nowStr == "<":
                if ptr > 0:
                    ptr -= 1
            elif nowStr == ">":
                if l > ptr:
                    ptr += 1
            elif nowStr == "-":
                if l >= ptr and ptr > 0:
                    ans[ptr - 1] = ""
                    ptr -= 1
            else:
                if l > ptr:
                    ans.insert(ptr, nowStr)
                else:
                    ans.append(nowStr)
                ptr+=1

        print("".join(ans))



# if __name__ == "__main__":
#     t = int(s.readline().rstrip())

#     for _ in range(t):
#         strings = [i for i in s.readline().rstrip()]

#         strings.reverse()

#         left = []
#         right = []

#         for _ in range(len(strings)):
#             nowStr = strings.pop()
            
#             if nowStr == "<":
#                 if left:
#                     right.append(left.pop())
#             elif nowStr == ">":
#                 if right:
#                     left.append(right.pop())
#             elif nowStr == "-":
#                 if left:
#                     left.pop()
#             else:
#                 left.append(nowStr)

#         print("".join(left),"".join(right[::-1]), sep="")     