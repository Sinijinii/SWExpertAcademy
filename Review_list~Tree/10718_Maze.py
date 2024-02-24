def Maze(N, arr):
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    s_xy = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                s_xy.append(i)
                s_xy.append(j)
    x = s_xy[0]
    y = s_xy[1]
    st = []
    while True:
        for idx in range(4):
            ni = x + di[idx]
            nj = y + dj[idx]
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] == 0:
                    st.append((x,y))
                    arr[ni][nj] = -1
                    x = ni
                    y = nj
                    break
                elif arr[ni][nj] == 3:
                    return 1
        else:
            if st:
                x,y = st.pop()
            else:
                break
    return 0

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]

    print(Maze(N,arr))


