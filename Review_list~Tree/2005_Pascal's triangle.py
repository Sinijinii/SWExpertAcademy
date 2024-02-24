T = int(input())
for tc in range(T):
    N = int(input())
    arr = [[1] * i for i in range(1,N+1)]
    for i in range(1,N):
        for j in range(1,len(arr[i])-1):
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

    print(f"#{tc+1}")
    for i in range(N):
        print(*arr[i])