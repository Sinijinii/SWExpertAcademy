from collections import deque

T = int(input())

for tc in range(T):
    #0은 통로, 1은 벽, 2는 출발, 3은 도착이다.
    N = int(input())

    arr = [list(map(int,list(input()))) for i in range(N)]
    st_i = 0
    st_j = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                st_i = i
                st_j = j
    # 이동할 네 방향 정의(상,하,좌,우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    Q = deque()
    Q.append([st_i,st_j])
    result = 0
    # 큐가 빌때까지 반복(queue가 비어있으면 나가진다)
    while Q:
        popdata = Q.popleft()
        x, y = popdata[0], popdata[1]
        #print("X,Y좌표 : ", x,y)
        # 현재 위치에서 네 방향으로 위치 확인
        for i in range(4):
            #print("i: ",i)
            nx = x + dx[i]
            ny = y + dy[i]
            #print("좌표 : ",nx,ny)
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            # 벽인 경우 무시
            if arr[nx][ny] == 1:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if arr[nx][ny] == 0:
                #print("0인 위치: ", nx,ny)
                count = str(arr[nx-dx[i]][ny-dy[i]]) + str(1)
                arr[nx][ny] = count
                Q.append([nx, ny])
            if arr[nx][ny] == 3:
                result = len(arr[nx-dx[i]][ny-dy[i]])-1
                Q.clear()
                break
    print(f"#{tc+1}",result)
    # deque에 아무값도 없어서 while문 탈출

