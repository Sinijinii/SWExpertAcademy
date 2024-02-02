# 십자
# T = int(input())
# for tc in range(T):
#     N,M = map(int, input().split())
#     arr_2 = []
#     for list_append in range(N):
#         arr_2.append(list(map(int, input().split())))
#     di = [0,1,0,-1]
#     dj = [1,0,-1,0]
#     di_list = []
#     dj_list = []
#     for num in range(1,M):
#         for idx in range(len(di)):
#             di_list.append(di[idx]*num)
#             dj_list.append(dj[idx]*num)
#     sum_list = 0
#     sum_result = 0
#     for i in range(N):
#         for j in range(N):
#             for k in range(len(di_list)):
#                 ni = i + di_list[k]
#                 nj = j + dj_list[k]
#                 if 0 <= ni < N and 0 <= nj < N:
#                     sum_list += arr_2[ni][nj]
#             print(sum_list)
#             if sum_result < sum_list:
#                 sum_result = sum_list
#             sum_list = 0
#     print(sum_result)


# 네모
T = int(input())
for tc in range(T):
    N,M = map(int,input().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int,input().split())))
    di = sum(list([n]*M for n in range(M)),[])
    dj = sum(list([n] for n in range(M)),[])*M
    sum_result = 0
    for i in range(N):
        for j in range(N):
            sum_list = 0
            for k in range(len(di)):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    sum_list += arr[ni][nj]
            if sum_list > sum_result:
                sum_result = sum_list
    print("#{}".format(tc + 1), sum_result)
