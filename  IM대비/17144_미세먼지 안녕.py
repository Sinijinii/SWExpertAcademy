R,C,T = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(R)]
di = [0,1,0,-1]
dj = [1,0,-1,0]

air_t = 0
air_u = 0

for num in range(T):
    arr_0 = [[0 for _ in range(C)] for __ in range(R)]
    for i in range(R):
        for j in range(C):
            cnt = 0
            for idx in range(4):
                if 0<=i + di[idx]< R and 0<= j + dj[idx] <C and arr[i][j] != -1:
                    if arr[i + di[idx]][j + dj[idx]] != -1:
                        arr_0[i+ di[idx]][j + dj[idx]] += arr[i][j] // 5
                        cnt += arr[i][j] // 5
            if arr[i][j] == -1 and air_t != 0:
                air_u = i
            elif arr[i][j] == -1 and air_t == 0:
                air_t = i

            arr_0[i][j] -= cnt
    for i_ in range(R):
        for j_ in range(C):
            arr[i_][j_] += arr_0[i_][j_]


    for c1 in range(air_t):
        if arr[air_t - c1][0] == -1:
            pass
        else:
            arr[air_t - c1][0] = arr[air_t - c1-1][0]
    for c2 in range(C-1):
        arr[0][c2] = arr[0][c2+1]
    for c3 in range(air_t):
        arr[c3][-1] = arr[c3+1][-1]
    for c4 in range(C-1):
        if arr[air_t][C-c4-2] ==-1:
            arr[air_t][C-c4-1] = 0
        else:
            arr[air_t][C-c4-1] = arr[air_t][C-c4-2]


    for c1 in range(air_u):
        if arr[air_u+c1][0] == -1:
            pass
        else:
            arr[air_u+c1][0] = arr[air_u+c1+1][0]
    for c2 in range(C-1):
        arr[-1][c2] = arr[-1][c2+1]
    for c3 in range(air_u):
        arr[air_u+air_u-c3][-1] = arr[air_u+air_u-c3-1][-1]

    for c4 in range(C-1):

        if arr[air_u][air_u+air_u-c4] == -1:
            arr[air_u][air_u+air_u-c4+1] = 0
        else:
            arr[air_u][air_u+air_u-c4+1] = arr[air_u][air_u+air_u-c4]

result = 2
for n in range(R):
    result += sum(arr[n])

print(result)