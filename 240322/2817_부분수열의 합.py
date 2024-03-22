def dfs(start,sum_data):
    global cnt
    # 기저조건
    if sum_data > K:
        return
    if sum_data == K:
        cnt += 1
        return
    if start < N:
        dfs(start + 1, sum_data+arr[start])
        dfs(start + 1, sum_data)



T =  int(input())
for tc in range(T):
    N,K = map(int,input().split())
    arr = list(map(int,input().split()))
    cnt = 0
    res = 0
    dfs(0,0)
    print(f"#{tc+1}",cnt)