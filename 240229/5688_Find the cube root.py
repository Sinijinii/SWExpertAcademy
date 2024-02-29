T = int(input())
for tc in range(T):
    N = int(input())
    e = int(round(N**(1/3),0))
    if e ** 3 == N:
        print(f"#{tc+1}",e)
    else:
        print(f"#{tc+1}",-1)
