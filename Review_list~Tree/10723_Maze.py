from collections import deque
def bfs(x,y):
    Q = deque()
    Q.append((x,y))
    visited[x][y] = 1
    result = 0
    while Q:
        x,y = Q.popleft()
        for i in range(4):
            # x + di[i]
            # y += dj[i]
            if 0 <= x + di[i] < N and 0 <= y + dj[i] < N:
                # 통로이면서
                if arr[x + di[i]][y + dj[i]] == 0:
                    # 방문한곳이 아니라면
                    if visited[x + di[i]][y + dj[i]] == 0:
                        # 방문 표시를 하고
                        visited[x + di[i]][y + dj[i]] = visited[x][y] + 1
                        # 큐에 좌표값을 넣어줌
                        Q.append((x + di[i],y + dj[i]))
                if arr[x + di[i]][y + dj[i]] == 3:
                    result = visited[x][y] - 1
                    return visited[x][y] - 1
    return result






T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                x = i
                y = j

    visited = [[0 for _ in range(N)] for __ in range(N)]
    # 상 하 좌 우
    di = [-1,1,0,0]
    dj = [0,0,-1,1]
    print(f"#{tc+1}",bfs(x,y))
