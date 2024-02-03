'''N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.
[입력]
첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 50 )
각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 1000 )
다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 1000000 )'''
# 내장함수 사용 금지
T = int(input())
for tc in range(T):
    N = int(input())
    min_value = 1000000 # 작은 값의 조건 할당( 1 ≤ ai≤ 1000000 )
    max_value = 1       # 큰 값의 조건 할당( 1 ≤ ai≤ 1000000 )
    arr = list(map(int, input().split()))
    for data in arr:    # 받은 값들을 비교하면서 값 할당
        if data > max_value:
            max_value = data
        if data < min_value:
            min_value  = data
    print(f'#{tc+1} {max_value-min_value}')