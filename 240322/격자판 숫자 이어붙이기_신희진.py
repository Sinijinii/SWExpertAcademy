def dfs(x,y,res_len):
    di = [0,0,1,-1]
    dj = [1,-1,0,0]
    # 기저조건
    if len(res_len) == 7:
        res.add(res_len)
        return

    for i in range(4):
        if 0 <= x + di[i] < 4 and 0 <= y + dj[i] < 4:
            dfs(x + di[i],y + dj[i],res_len+arr[x + di[i]][y + dj[i]])
        else:
            continue


T = int(input())
for tc in range(T):
    arr = [input().split() for _ in range(4)]
    res = set()
    for i in range(4):
        for j in range(4):
            dfs(i,j,arr[i][j])

    print(f"#{tc+1}",len(res))