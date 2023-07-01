from sys import stdin as s

s = open("input.txt", "rt")


if __name__ == "__main__":
    n = int(s.readline().strip())
    cars = [list(map(int, a.split(" "))) for a in s.readlines()]

    finals = dict()

    for i in range(n):
        now_car = cars[i]

        if now_car[0] in finals.keys():

            if finals[now_car[0]][1] < now_car[1]:
                finals[now_car[0]] = now_car + [i + 1]
        else:
            finals[now_car[0]] = now_car + [i + 1]


    sum = 0

    for value in finals.values():
        sum += value[2]

    print(sum)