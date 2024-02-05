'''1부터 12까지의 숫자를 원소로 가진 집합 A가 있다. 집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수를 출력하는 프로그램을 작성하시오.
해당하는 부분집합이 없는 경우 0을 출력한다. 모든 부분 집합을 만들어 답을 찾아도 된다.
 예를 들어 N = 3, K = 6 경우, 부분집합은 { 1, 2, 3 } 경우 1가지가 존재한다.'''
T = int(input())
for tc in range(T):
    N,K = map(int,input().split())
    # 조건에 맞는 data생성 -> 1부터 12까지의 숫자를 원소로 가진 집합 A
    arr = list(range(1,13))
    N_arr = len(arr)
    # 개수를 구해줄 값 result
    result = 0
    # 비트 연산자를 이용하여 부분집합 구하기
    for i in range(1<<12):          # 부분집합의 개수(2의n승)만큼 돌림/ 부분집합을 구하기 위한 길이
        list_data = []              # 부분집합을 담을 리스트 생성
        sum_data = 0                # 부분집합의 합을 구할 변수
        for j in range(N_arr):      # 아래 부분도 range(arr의 길이)임 -> 그냥 arr가 들어가면 안됨
            if i & (1<<j):          # 부분집합에 맞는 값 구하기 -> 이때 arr[j]가 부분집합의 원소
                list_data.append(arr[j])
                sum_data += arr[j]  # 부분집합의 합

            len_data = 0            # 부분집합의 길이 구하는 곳
            for data in list_data:
                len_data += 1

        # 조건에 맞는 경우 result에 +1
        if len_data == N and sum_data == K:
            result += 1

    print(f'#{tc+1} {result}')

