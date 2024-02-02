'''
9
7 4 2 0 0 6 0 7 0
'''
#
# N = int(input())
# arr = list(map(int, input().split()))
#
# max_v = 0 # 가장 큰 낙차
# for i in range(N-1):    # for i : 0 -> N-1 낙차를 구할 위치
#     cnt = 0             # 오른쪽에 있는 더 낮은 높이의 개수
#     for j in range(i+1,N):  # for j : i+1 -> N-1
#         if arr[i]>arr[j]:
#             cnt += 1
#     if max_v < cnt:     # 최대 낙차보다 크면
#         max_v = cnt
# print(max_v)

# 버블정렬
# N = 6
# arr = [7,2,5,3,1,4]
#
# for i in range(N-1,0,-1):
#     for j in range(i):
#         if arr[j] > arr[j+1]:
#             arr[j],arr[j+1] = arr[j+1], arr[j]
# print(arr)

# 카운팅 정렬
N = 6
K = 9
data = [7,2,4,5,8,3]
counts = [0] * (K+1)
temp = [0] * N
# counts 배열에 기록
for x in data:
    counts[x] += 1
# counts 누적합
for i in range(1,K):
    counts[i] += counts[i-1]
# data의 마지막 원소부터 정렬
for i in range(N-1,-1,-1): # N-1 -> 0
    counts[data[i]] -= 1
    temp[counts[data[i]]] = data[i]
print(*temp)