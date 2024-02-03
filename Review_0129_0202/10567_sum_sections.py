T = int(input())
for tc in range(T):
    N,M = map(int,input().split()) # 정수의 개수 N, 구간의 개수 M
    arr = list(map(int,input().split())) # N개의 정수
    idx = N - M + 1     # 이웃한 수의 합을 구하기 위한 반복 횟수

    min_result = 100000 * 100  # 최소값을 구할 변수 생성 _ 조건 확인
    max_result = 0  # 최대값을 구할 변수 생성
    for i in range(idx):
        sum_data = 0  # 값을 더할 변수 생성 / 한번 돌고 나서 초기화
        for num in range(M):
            sum_data += arr[i + num]    # 조건에 맞는 값을 더해줌
        if sum_data > max_result:
            max_result = sum_data
        if sum_data < min_result:
            min_result = sum_data

    print(f'#{tc+1} {max_result - min_result}')
