memo = dict()

def fibonacci_recursion(n) -> int:


    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursion(n-2) + fibonacci_recursion(n-1)

def fibonacci_memo(n) -> int:


    if n in memo:
        return memo[n] #딕셔너리에 이미 계산된 결과가 있으면 그 값을 리턴
    elif n <= 1:
        return n
    else:
        memo[n] = fibonacci_memo(n-2) + fibonacci_memo(n-1)
        return memo[n]



n = int(input())
print(fibonacci_recursion(n))
print(fibonacci_memo(n))