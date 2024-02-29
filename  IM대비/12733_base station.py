T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    H_count = 0
    cover_H_count = 0
    distance = {'A':1,'B':2,'C':3}
    di = [-1,0,1,0]
    dj = [0,1,0,-1]
    for i in range(N):
        for j in range(N):
            if arr[i][j] in "H H2":
                H_count+=1
            if arr[i][j] in "ABC":
                for idx in range(4):
                    for n in range(1,distance[arr[i][j]]+1):
                        ni = i+(di[idx]*n)
                        nj = j+(dj[idx]*n)
                        if 0<= ni < N and 0<=nj<N and arr[ni][nj] =="H":
                            arr[ni][nj] = "H2"
                            cover_H_count += 1
    print(f"#{tc+1}",H_count-cover_H_count)