T = int(input())
for tc in range(T):
    # 최대 이동거리 K, 종점 번호 N, 충전기의 수 M
    K,N,M = map(int,input().split())
    # 충전기의 위치 값
    charger = list(map(int,input().split()))
    # 0인 값들 중 충전기의 위치에만 1로 표시
    arr = [0] * (N+1)
    for cg_idx in charger:
        arr[cg_idx] = 1
    #나의 위치 idx, 충전의 횟수 count 변수
    idx = 0
    count = 0

    while True:
        # 충전기를 하나도 찾지 못한 경우를 구하기 위한 zero_count변수
        zero_count = 0
        # 뒤에서부터 돌며 만약 충전기를 찾았다면 count를 +1하고 나의 위치를 변경시켜준 후 for문을 나옴
        for step in range(K,0,-1):
            if arr[idx + step] == 1:
                count += 1
                idx = idx + step
                break
            # 만약 충전기를 찾지 못했다면 zero_count에 +1
            else :
                zero_count += 1
        # for문을 한번 다 순회하였다면
        # 충전기를 찾지 못한 횟수가 최대 이동거리보다 크거나 같다면 이동이 불가능 함으로 count를 0으로 반환
        if zero_count >= K:
            count = 0
        # 종점에 도착하였거나, 충전실패인 경우 while문을 빠져나옴
        if idx+K >= N or zero_count >= K:
            break
    print(f'#{tc+1} {count}')