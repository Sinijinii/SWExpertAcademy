T = 10
for tc in range(T):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    cnt = 0
    for j in range(N):
        ns = 0
        for i in range(N):
            if arr[i][j] == 1:
                ns = 1
            elif ns == 1 and arr[i][j] == 2:
                cnt += 1
                ns = 0

    print(f"#{tc+1}",cnt)