

arr = [2, 55, 12, 54, 22]

# 최댓값을 구하는 재귀 함수 (O(2**n))
# def max(arr):
#     print("recursion")

#     if len(arr) == 1:
#         return arr[0]
    
#     if arr[0] > max(arr[1:]):
#         return arr[0]
#     else:
#         return max(arr[1:])
    
# 최댓값을 구하는 재귀함수 O(n)
# def max(array):
#     print("recursion")

#     if len(array) == 1:
#         return array[0]
    
#     max_of_remainder = max(array[1:])

#     if array[0] > max_of_remainder:
#         return array[0]
#     else:
#         return max_of_remainder
    
# def fib(n):
# 	# 기저 조건은 수열의 처음 두 수다.
# 	if n == 0 or n == 1:
# 		return n
# 	# 앞의 두 피보나치 수의 합을 반환한다.
# 	else:
# 		return fib(n-2) + fib(n-1)

# def fib(n, memo):
	
#     if n == 0 or n == 1:
#         return n
    
#     if not memo.get(n):
#         memo[n] = fib(n-2, memo) + fib(n-1, memo)
    
#     return memo[n]

# 상향식을 통한 피보나치 수열
# def fib(n):
#     if n == 0:
#         return 0
    
#     for i in range(n):
#         temp = a
#         a = b
#         b = temp + a

#     return b

""" 
연습 문제 1 

다음 함수는 수 배열을 받아서 그 합을 반환하되 합이 100을 초과하게 만드는 수는 제외한다.
어떤 수를 더해서 합이 100이 넘으면 그 수는 무시한다. 하지만 함수에서 불필요한 재귀 호출이 일어나고 있다.
코드를 수정해서 불필요한 재귀 호출을 없애자

"""

def add_until_100(array):
    print("recursion")

    if len(array) == 0:
        return 0
    
    if array[0] + add_until_100(array[1:]) > 100:
        return add_until_100(array[1:])
    else:
        return array[0] + add_until_100(array[1:])

def add_until_100_2(array):
    print("recursion")

    if len(array) == 0:
        return 0
    
    sum_of_remain_numbers = add_until_100(array[1:])

    if array[0] + sum_of_remain_numbers > 100:
        return add_until_100(array[1:])
    else:
        return arr[0] + sum_of_remain_numbers

# print(add_until_100(arr))
# print(add_until_100_2(arr))

""" 
연습 문제 2 

다음의 함수는 재귀를 사용해 골롬 수열이라는 수학적 수열의 N번째 수를 계산한다.
하지만 형편없이 비효율적이다. 메모이제이션으로 최적화하자 
"""

golombs = {}
golombs[1] = 1
golombs[2] = 2
golombs[3] = 2

def golomb(n):
    print("recursion")

    if n == 1:
        return 1
    else:
        return 1 + golomb(n - golomb(golomb(n - 1)))

def golomb2(n, memo = {}):
    print("recursion")

    if n == 1:
        return 1
    if not memo.get(n):
        memo[n] = 1 + golomb2(n - golomb2(golomb2(n -1, memo), memo), memo)

    return memo[n]

# print(golomb(5))
# print(golomb2(5))


""" 
연습 문제 3 

다음은 11장 연습 문제에 나왔던 "유일 경로" 문제의 해법이다. 메모이제이션으로 효율성을 개선하자.
"""

def unique_path(r, c, memo = {}):
    if r == 1 or c == 1:
        return 1

    if not memo.get((f"{r}and{c}")):
        memo[f"{r}and{c}"] = unique_path(r - 1, c, memo) + unique_path(r, c - 1, memo)

    return memo[f"{r}and{c}"]

# print(unique_path(3, 7))