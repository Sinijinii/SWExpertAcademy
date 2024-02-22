T = int(input())
for tc in range(T):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    for i in range(N):
        for j in range(N):
            sum_data = 0
            for idx_x in range(-M,M+1):
                for idx_y in range(-M,M+1):
                    if 0 <= i+idx_x < N and 0 <= j+idx_y < N:
                        sum_data += arr[i][j+idx_y]
                        sum_data += arr[i+idx_x][j]
            print(sum_data)
