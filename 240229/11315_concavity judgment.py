T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    di = [0,1,1,-1]
    dj = [1,0,1,1]

    n = False
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                for idx in range(4):
                    cnt = 1
                    for num in range(1,5):
                        if 0<= i + di[idx]*num < N and 0<=j + dj[idx]*num < N and arr[i + di[idx]*num][j + dj[idx]*num] == 'o':
                            pass
                        else:
                            break
                    else: n = True

    if n:
        result = "YES"
    else:
        result = "NO"
    print(f"#{tc+1}",result)