from collections import deque

def bfs(N):
    Q = deque()
    Q.append((N,1))
    vis[N] = 1

    while Q:
        n,cnt = Q.popleft()

        fm = [n + 1, n - 1, n * 2, n - 10]
        for i in fm:
            if i == M:
                return cnt
            if 1 <= i <= 1000000 and vis[i] == 0:
                Q.append((i,cnt+1))
                vis[i] = 1


T = int(input())
for tc in range(T):
    N,M = map(int,input().split())
    vis = [0 for i in range(1000001)]
    print(f"#{tc+1}",bfs(N))