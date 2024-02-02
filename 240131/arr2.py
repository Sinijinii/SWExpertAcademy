# N = int(input())
# arr = [[0]*3 for _ in range(N)]
# # print(arr)
#
# i = 3
# j = 4
# di = [0,1,0,-1]
# dj = [1,0,-1,0]
#
# for k in range(4):
#     ni = i+di[k]
#     nj = j+dj[k]
#     print(ni,nj)
# print("--------------2차원--------------")
# # 2차원
# N = 5
# arr_2 = [[0]*N for _ in range(N)]
# for i in range(N):
#     for j in range(N):
#         for k in range(4):
#             ni = i + di[k]
#             nj = j + dj[k]
#             if 0 <= ni < N and 0 <= nj < N:
#                 print((arr_2[ni][nj]),end=" ")
#         print()
#
# # 2차원
# N = 5
# arr_2 = [[0]*N for _ in range(N)]
# for i in range(N):
#     for di,dj in [[0,1],[1,0],[0,-1],[-1,0]]:
#         ni,nj = i+di, j+dj
#         if 0 <= ni < N and 0 <= nj < N:
#             print((arr_2[ni][nj]), end=" ")


#-------------------------------------------------------------

arr = [3,6,7,1,5,4]
n = len(arr)                     # 원소의 개수
for i in range(1<<n):            # 1<<n: 부분집합의 개수
    for j in range(n):             # 원소의 수만큼 비트 비교
        if i & (1<<j):               # i의 j번 비트가 1인 경우
            print(arr[j], end = ' ')     # j번 원소 출력

    print()

# 부분집합 합 문제 구현하기
