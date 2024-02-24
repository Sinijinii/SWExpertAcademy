def dfs(s):
    vis[s] = 1
    stack = []
    while True:
        for idx in adj[s]:
            if vis[idx] == 0:
                vis[idx] = 1
                s = idx
                stack.append(idx)
                break
        else:
            if len(stack) > 0:
                s = stack.pop()
            else:
                break

T = 10
for tc in range(T):
    tc_num,N = map(int,input().split())
    arr = list(map(int,input().split()))
    adj = [[] for _ in range(100)]
    for i in range(0,N*2,2):
        adj[arr[i]].append(arr[i+1])
    vis = [0] * 100
    for j in range(len(adj)):
        if len(adj[j]) > 0:
            s = j
            break
    dfs(s)
    print(f"#{tc+1}",vis[99])
