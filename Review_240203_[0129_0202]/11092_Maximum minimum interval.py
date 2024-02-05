# T = int(input())
# for tc in range(T):
#     N = int(input())
#     arr = list(map(int,input().split()))
#     minimum = N # 조건에 해당하는 값 설정
#     maximum = N
#     for idx in range(N):
#         if arr[minimum-1] > arr[idx]:  # 작은수가 여러개면 먼저 나오는 위치를 반환 (초과)
#             minimum = idx+1
#         if arr[maximum-1] <= arr[idx]: # 큰수가 여러개면 뒤에 나오는 위치를 반환(이하)
#             maximum = idx+1
#
#     print(f'#{tc+1} {maximum-minimum}')

 #list(filter(lambda x: data[x] == min_data, range(len(data))))를 사용
T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int,input().split()))
    minimum = 10    # 조건에 해당하는 값 설정 ( 1 ≤ ai≤ 10 )
    maximum = 1     # 조건에 해당하는 값 설정 ( 1 ≤ ai≤ 10 )
    # 최대 최소값 구하기
    for data in arr:
        if data > maximum:
            maximum = data
        if data < minimum:
            minimum = data
    # 최대 최소가 있는 인덱스 값 구하기 - 순서대로 출력됨
    max_idx_list = list(filter(lambda x : arr[x] == maximum, range(N)))
    min_idx_list = list(filter(lambda x : arr[x] == minimum, range(N)))
    print(f'#{tc+1} {abs(max_idx_list[-1]-min_idx_list[0])}')

