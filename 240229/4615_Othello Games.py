T = int(input())
# 오른쪽부터 시계방향으로 방향을 탐색할 수 있는 델타 생성
di = [0, 1, 1, 1, 0, -1, -1, -1]
dj = [1, 1, 0, -1, -1, -1, 0, 1]
op = [0, 2, 1]


def find_flip(i, j, wb):
    board[i][j] = wb
    for d in range(8):
        tmp_flip_li = []
        ni, nj = i + di[d], j + dj[d]
        while 0 <= ni < N and 0 <= nj < N and board[ni][nj] == op[wb]:
            tmp_flip_li.append((ni, nj))
            ni, nj = ni + di[d], nj + dj[d]
        if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == wb:
            for p, q in tmp_flip_li:
                board[p][q] = wb


for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # 한변의 길이 N,플레이어가 돌을 놓는 횟수 M
    mid = N // 2
    board = [[0] * N for _ in range(N)]
    board[mid - 1][mid - 1] = 2
    board[mid][mid] = 2
    board[mid - 1][mid] = 1
    board[mid][mid - 1] = 1

    for _ in range(M):
        x, y, color = map(int, input().split())
        # 인덱스로 변환시켜준다.
        x = x - 1
        y = y - 1
        find_flip(y, x, color)
    b_cnt = 0
    w_cnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                b_cnt += 1
            elif board[i][j] == 2:
                w_cnt += 1
    print(f'#{tc}', b_cnt, w_cnt)