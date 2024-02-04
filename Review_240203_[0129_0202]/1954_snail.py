T = int(input())
for tc in range(T):
    N = int(input())
    # 우, 하, 좌, 상에 대한 xy 이동 좌표
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    # 각 길이에 해당하는 2차원 배열 생성
    arr = list([0]*N for i in range(N))
    # 첫 시작 좌표 0,0
    idx_x,idx_y = 0,0
    # 첫 시작 좌표의 값 1
    arr[0][0] = 1
    # 더해주며 할당할 변수 생성 [0][0]의 값이 1로 시작되므로 초기값 1
    sum_data = 1
    # xy이동에 필요한 변수
    x_y = 0
    turn = True
    # 결과가 나오고 while문이 종료되므로 N*N+1이 아닌 N*N에서 멈춤
    while sum_data < N*N:
        # 좌표 이동
        idx_x += di[x_y]
        idx_y += dj[x_y]
        # 좌표를 이동한 값이 0보다 크고 리스트의 길이 만큼보다는 작으며, 그 값이 0인 경우에만 값을 할당
        if idx_x >= 0 and idx_x < N and idx_y >= 0 and idx_y < N and arr[idx_x][idx_y] == 0:
            sum_data += 1
            arr[idx_x][idx_y] = sum_data
        # 그외의 경우에는 다시 좌표값을 이전으로 돌려놓고, 위치 좌표가 3인경우엔 처음부터, 그 외엔 +1을해주며 우,하,좌,상 반복
        else :
            idx_x -= di[x_y]
            idx_y -= dj[x_y]
            if x_y == 3:
                x_y = 0
            else:
                x_y += 1

    print('#{}'.format(tc+1))
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end =" ")
        print()
