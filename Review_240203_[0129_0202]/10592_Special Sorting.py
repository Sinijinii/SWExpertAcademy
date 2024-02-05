'''N개의 정수가 주어지면 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로 큰 수와 작은 수를 번갈아 정렬하는 방법이다'''
T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))


# # 카운팅정렬
#     # 각 숫자의 개수
#     counting = [0] * 100  # 1<=ai<=100
#     temp = [0] * N
#     for i in arr:
#         counting[i] += 1
#
#     # 누적합
#     for cnt in range(1,len(counting)):
#         counting[cnt] += counting[cnt-1]
#
#     # 위치 할당 -> 뒤에서 부터
#     # 오름차순
#     for i in range(N-1,-1,-1):
#         counting[arr[i]] -= 1
#         temp[counting[arr[i]]] = arr[i]

# 버블정렬
    for i in range(N-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

    result = []
    idx = -1
    # -1,0,-2,1,-3,2,... > 10개
    for i in range(1,11):
        result.append(arr[idx])
        if i % 2 == 0:
            idx -= i
        else : idx += i
    print("#{}".format(tc + 1), *result)


