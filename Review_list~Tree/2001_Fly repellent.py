
T = int(input())
for tc in range(T):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    # 최종 값을 담을 변수
    result = 0
    # 변의 길이 - 파리채의 크기 + 1 만큼 돌기
    for i in range(N-M +1):
        for j in range(N-M +1):
            # 파리채로 잡는 파리의 수를 구할 변수
            sum_data = 0
            # 파리채의 길이만큼 돌기
            for idx in range(M):
                for idx_y in range(M):
                    # 더해줌
                    sum_data += arr[i+idx][j+idx_y]
            # 결과값 비교
            if sum_data > result:
                result = sum_data
    print(f"#{tc+1}",result)


