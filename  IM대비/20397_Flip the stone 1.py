T = int(input())
for tc in range(T):
    N,M = map(int,input().split())
    stone = list(map(int,input().split()))
    for num in range(M):
        i,j = map(int,input().split())
        for st in range(j):
            if 0 <= i-1+st < N:
                stone[i-1+st] = stone[i-1]
    print(f"#{tc+1}",*stone)