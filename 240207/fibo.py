# 일반적인 재귀호출을 사용한 피보나치
def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1)+fibo(n-2)

# 메모이제이션
def fibo_memo(n):
    global memo
    if n >= 2 and memo[n] == 0:
        memo[n] = fibo_memo(n-1) + fibo_memo(n-2)
    return  memo[n]


n = 7
memo = [0] * (n+1)
memo[0] = 0
memo[1] = 1