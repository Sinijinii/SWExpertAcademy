def f(i,k):
    global min_v
    if i == k:
        #print(*P)
        s = 0 #선택한 원소의 합
        for j in range(k):
            s += arr[j][P[j]]
        if min_v > s:
            min_v = s
    else:
        # P[i]자리로 바꿀(올)원소 P[j]
        for j in range(i,k):
            # P[i] <->P[j]
            P[i],P[j] = P[j],P[i]
            f(i+1,k)
            P[i],P[j] = P[j],P[i] # 교환전으로 복구


T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    P = [i for i in range(N)]
    min_v = 9*N
    f(0,N)
    print(f"#{tc+1}", min_v)





#########################################################################################
# def f(i,k,s):
#     global cnt
#     global min_v
#     cnt += 1
#     if i == k:
#         if min_v > s:
#             min_v = s
#     elif s >= min_v:
#         return
#     else:
#         # P[i]자리로 바꿀(올)원소 P[j]
#         for j in range(i,k):
#             # P[i] <->P[j]
#             P[i],P[j] = P[j],P[i]
#             f(i+1,k,s)
#             P[i],P[j] = P[j],P[i] # 교환전으로 복구
#
#
# N = 3
# arr = [list(map(int, input().split())) for _ in range(N)]
# P = [i for i in range(N)]
# min_v = 9*N
# cnt = 0
# f(0,N,0)
# print(min_v,cnt)
