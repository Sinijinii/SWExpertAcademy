T = int(input())
for tc in range(T):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    di = [1,0,-1,0]
    dj = [0,1,0,-1]
    result = 0
    for i in range(N):
        for j in range(M):
            sum_data = arr[i][j]
            for idx in range(4):
                for num in range(1,arr[i][j]+1):
                    if 0 <= i+(di[idx]*num) < N and 0 <= j+(dj[idx]*num) < M:
                        #print(i+(di[idx]*num),j+(dj[idx]*num))
                        sum_data += arr[i+(di[idx]*num)][j+(dj[idx]*num)]

            if result < sum_data:
                result = sum_data
    print(f"#{tc+1}",result)
