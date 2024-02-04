T = int(input())
for tc in range(T):
    N = int(input())
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    arr = list([0]*N for i in range(N))
    x,idx_y = 0,0
    arr[0][0] = 1
    sum_data = 1
    x_y = 0
    turn = True
    while sum_data < N*N-1:
        idx_x = di[x_y] + x
        idx_y = dj[x_y] + y

        if idx_x >= 0 and idx_x < N and idx_y >= 0 and idx_y < N and arr[idx_x][idx_y] == 0:
            sum_data += 1
            arr[idx_x][idx_y] = sum_data
            x = idx_x
            y = idx_y

        else :
            x_y = (x_y+1)%4
        print(x_y)
        print(idx_x, idx_y, sum_data)

    print(arr)




    # print('#{}'.format(tc+1))
    # for i in range(N):
    #     for j in range(N):
    #         print(arr[i][j], end =" ")
    #     print()
