from collections import deque

def bfs(x,y):
    res = 1
    di = [0,0,1,-1]
    dj = [1,-1,0,0]
    q = deque()
    q.append((x,y))
    while q:
        xi,yj= q.popleft()
        for i in range(4):
            if 0 <= xi+di[i] <N and 0 <= yj+dj[i] <N:
                if arr[xi+di[i]][yj+dj[i]] == arr[xi][yj] + 1:
                    q.append((xi+di[i],yj+dj[i]))
                    res += 1
    return arr[x][y],res




T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    res_li = []
    for i in range(N):
        for j in range(N):
            res_li.append(bfs(i,j))
    res_li = sorted(res_li,key = lambda x:(-x[1],x[0]))
    print(f"#{tc+1}",*res_li[0])
