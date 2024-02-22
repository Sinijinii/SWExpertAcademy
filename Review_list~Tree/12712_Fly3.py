T = int(input())
for tc in range(T):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    di2 = [-1,1,1,-1]
    dj2 = [1,1,-1,-1]
    result = 0
    for i in range(N):
        for j in range(N):
            # 플러스 모양, x자 모양의 합
            pl_data = 0
            x_data = 0
            for idx in range(4):
                for c in range(1,M):
                    if 0 <= i+(di[idx]*c) < N and 0<=j+(dj[idx]*c)<N:
                        pl_data += arr[i+(di[idx]*c)][j+(dj[idx]*c)]
                        #print(" 십자: ",i+(di[idx]*c),j+(dj[idx]*c))
                        # print()
                    if 0 <= i+(di2[idx]*c) < N and 0<=j+(dj2[idx]*c)<N:
                        # 대각선
                        x_data += arr[i+(di2[idx]*c)][j+(dj2[idx]*c)]
                        # print(" 대각선: ",i+(di2[idx]*c),j+(dj2[idx]*c))
            pl_data += arr[i][j]
            x_data += arr[i][j]
            if x_data < pl_data:
                max_data = pl_data
            else:
                max_data = x_data
            if result < max_data:
                result = max_data
    print(f"#{tc+1}",result)


