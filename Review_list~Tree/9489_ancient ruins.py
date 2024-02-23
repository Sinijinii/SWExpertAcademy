T = int(input())
for tc in range(T):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    for i in range(N):
        aL = [arr[i][0]]
        L = 0
        w = 0
        for j in range(M):

            if len(aL) == 1 or (aL[-1] == 1 and arr[i][j] ==1) :
                aL.append(arr[i][j])
                L += 1
            # if len(aw) == 1 or (aw[-1] == 1 and arr[j][i] ==1) :
            #     aw.append(arr[j][i])
            #     w += 1

        print(aL)
        print(L)
        # print(aw)
        # print(w)
    print()