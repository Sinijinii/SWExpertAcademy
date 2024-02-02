def rotation(arr):
    arr_ro = []
    for i in range(N):
        arr_3 = []
        for j in range(N):
            arr_3.append(arr[N - j - 1][i])
        arr_ro.append(arr_3)
    return arr_ro

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    arr_90 = rotation(arr)
    arr_180 = rotation(arr_90)
    arr_270 = rotation(arr_180)
    print("#{}".format(tc+1))
    for i in range(N):
        for j in range(N):
            print(arr_90[i][j], end="")
        print(end=" ")
        for j in range(N):
            print(arr_180[i][j], end="")
        print(end=" ")
        for j in range(N):
            print(arr_270[i][j], end="")
        print(end=" ")
        print()

