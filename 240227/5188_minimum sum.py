def minimum(s_x,s_y,sum_data):
    global result
    sum_data += arr[s_x][s_y]
    di = [0,1]
    dj = [1,0]

    if s_x == N-1 and s_y == N-1:
        if result > sum_data:
            result = sum_data
    for i in range(2):
        if 0 <= s_x + di[i] < N and 0<= s_y + dj[i] < N:
            r_s_x = s_x + di[i]
            r_s_y = s_y + dj[i]
            minimum(r_s_x,r_s_y,sum_data)


T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    path = []
    sum_data = 0
    result = 10*N
    minimum(0,0,0)
    print(f"#{tc+1}",result)
