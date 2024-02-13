T = int(input())

def maze(N, arr):
    st_i = 0
    st_j = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == '2':
                st_i = i
                st_j = j
    stack = []
    # 아래,우, 좌, 위
    di = [1, 0, 0, -1]
    dj = [0, 1, -1, 0]
    while True:
        for d in range(4):
            ni = st_i + di[d]
            nj = st_j + dj[d]
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] == '0':
                    stack.append((st_i, st_j))
                    arr[ni][nj] = -1
                    st_i = ni
                    st_j = nj
                    break
                elif arr[ni][nj] == '3':
                    return 1
        else:   # for문의 else -> break와 return으로 끝나지 않은 경우 > 벽에 걸리거나, 왔던 곳인 경우
            # 스택에 값이 있는 경우 : 왔었던 길인 경우 다시 되돌아감
            if stack:
                st_i, st_j = stack.pop()
            else:
                break
    return 0


for tc in range(T):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    print(f'#{tc+1} {maze(N,arr)}')



