def Queen(i, N):  # i 행에 퀸을 놓는 함수
    global cnt
    if i == N:
        cnt += 1
        return  # 모든 행에 퀸을 놓은 경우
    else:
        # i행 j열 에 퀸을 놓을 수 있는 조건
        # j열에 다른 퀸이 없어야함, 왼쪽 위, 오른쪽 위 대각선 상에도 없어야 함
        for j in range(N):
            if col[j] == 0 and dia1[i + j] == 0 and dia2[N - 1 + i - j] == 0:
                col[j] = 1
                dia1[i + j] = 1
                dia2[N - 1 + i - j] = 1
                # bd[i][j] = 1
                Queen(i + 1, N)  # 다음 행으로 이동
                # bd[i][j] = 0    # i행에서 이전에 놨던 퀸 삭제
                col[j] = 0
                dia1[i + j] = 0
                dia2[N - 1 + i - j] = 0


T = int(input())
for tc in range(T):
    N = int(input())

    bd = [[0] * N for _ in range(N)]
    col = [0] * N  # 특정 열에 퀸이 있음을 표시
    dia1 = [0] * (N + N - 1)
    dia2 = [0] * (2 * N)
    cnt = 0
    Queen(0, N)
    print(f'#{tc+1}',cnt)