def dfs_permutation(level,N,value):
    global result
    if value <= result:
        return

    if level == N:
        if result < value:
            result = value
        return

    for i in range(len(P)):
        if P[i] in vis:
            continue
        vis[level] = P[i]
        next_pr = value * (arr[level][P[i]] / 100)

        dfs_permutation(level + 1,N,next_pr)
        vis[level] = N

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    P = [i for i in range(N)]

    vis = [N] * N
    result = 0
    dfs_permutation(0,N,1)
    print(f"#{tc+1} {round(result*100,6):.6f}")