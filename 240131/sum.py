T = 10 # 테스트 케이스의 개수
for tc in range(T):
    N = int(input())
    # 이중리스트
    arr = [list(map(int,input().split())) for _ in range(100)]
    # 최종 최대값 받을 result
    result = 0
    # 정방향 대각선, 역방향 대각선
    sum_z = 0
    sum_z_b = 0
    for i in range(100):
        # 행, 열
        sum_i = 0
        sum_j = 0
        # 대각선 값을 더해줌
        sum_z += arr[i][i]
        sum_z_b += arr[i][99-i]

        for j in range(100):
            # 행과 열의 값을 더해줌
            sum_i += arr[i][j]
            sum_j += arr[j][i]
        # 값들 비교 후 가장 큰 값을 result에 반환
        if sum_i > result:
            result = sum_i
        if sum_j > result:
            result = sum_j
        if sum_z > result:
            result = sum_z
        if sum_z_b > result:
            result = sum_z_b
    print("#{}".format(tc + 1), result)
