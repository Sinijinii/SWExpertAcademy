def DP_f():
    # 가로 0, 대각선 1, 세로 2
    DP[0][0][1] = 1
    for idx in range(2, N):
        if arr[0][idx] == 0:
            DP[0][0][idx] = DP[0][0][idx-1]

    for i in range(1,N):
        for j in range(1,N):
            # 대각선의 경우
            # 옆 아래 대각선이 비어있어야함 > 전의 값을 가져옴 가로 세로 대각선이 가능
            if arr[i][j] == 0 and arr[i-1][j] == 0 and arr[i][j-1] == 0:
                DP[1][i][j] = DP[1][i-1][j-1] + DP[2][i-1][j-1] + DP[0][i-1][j-1]

            # 가로 세로
            if arr[i][j] == 0:
                DP[0][i][j] = DP[0][i][j-1] + DP[1][i][j-1]
                DP[2][i][j] = DP[2][i-1][j] + DP[1][i-1][j]
    return DP


N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
DP = [[list(0 for _ in range(N))for __ in range(N)] for ___ in range(N)]
result_dp = DP_f()
result = 0
for i in range(N):
    result += result_dp[i][N-1][N-1]

print(result)