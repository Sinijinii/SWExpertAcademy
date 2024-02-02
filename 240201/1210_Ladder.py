T = 10
for tc in range(T):
    N = int(input())
    arr = []
    for _ in range(100):
        arr.append(list(map(int,input().split())))
    fin_idx = arr[99].index(2)
    i = 99
    j = fin_idx
    di = [0, 0,-1]
    dj = [-1, 1, 0]
    print(i,j)
    while i>=0 and j>=0:
        for idx in range(len(di)):
            print()
            if (arr[i + di[idx]][j + dj[idx]] == 1) and j + dj[idx] >= 0:
                arr[i][j] = 0
                print(i + di[idx], j + dj[idx])
                if j + dj[idx] >= 0 or j + dj[idx] <= 99:
                    i = i + di[idx]
                    j = j + dj[idx]
                else: continue
                if i == 0:
                    break
            continue
    print("Result : ",j)

