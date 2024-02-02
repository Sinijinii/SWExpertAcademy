T = int(input())
di = [0,1,0,-1]
dj = [1,0,-1,0]
di_list = []
for tc in range(T):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    sum_data = 1
    i = 0
    j = 0
    count_data = 0
    for n in range(N*2-1):
        if n == 0:
            arr[0][0] = 1
            sum_data += 1
        else:


            for idx in range(len(di)):
                print(N)
                for __ in range(N-1):
                    i += di[idx]
                    j += dj[idx]
                    print(i, j, idx)
                    arr[i][j] = sum_data
                    sum_data += 1
                    count_data += 1
                    if count_data == (N-1)*3:
                        N -= 1
                print(arr)









