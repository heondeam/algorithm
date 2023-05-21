from sys import stdin as s
import math

s = open("input.txt", "rt")
""" 1475. 방 번호 """


# 1,000,000 보다 작은 수의 방 번호가 주어졌을 때 
# 0 ~ 9 까지 있는 숫자 세트로 방 번호를 표현하려고 한다.
# 필요한 숫자 세트의 최솟값을 구하자 (6 = 9, 9 = 6) 
# 그러므로 한 숫자 세트당 표현할 수 있는 숫자는 0,1,2,3,4,5,6,6,6,6,7,8

if __name__ == "__main__":
    n = [int(num) for num in s.readline().rstrip()]

    cards = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0, 
        6: 0,
        7: 0,
        8: 0
    }

    for i in n:
        if i == 9:
            cards[6] += 1
        else:
            cards[i] += 1

    if (max(cards.values()) == cards[6]):
        cards[6] = math.ceil(cards[6]/2)
        print(max(cards.values()))
        
    else:
        print(max(cards.values()))