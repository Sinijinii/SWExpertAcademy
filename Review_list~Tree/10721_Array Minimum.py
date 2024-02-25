# def f(i,N):
#     global min_v
#     if i == N:
#         for idx in range(N):
#             print(idx,P[idx])
#             print(arr[idx][P[idx]])
#     else:
#         for idx in range(i,N):
#             P[i],P[idx] = P[idx],P[i]
#             f(i+1,N)
#             P[i], P[idx] = P[idx], P[i]
#
# T = int(input())
# for tc in range(T):
#     N = int(input())
#     arr = [list(map(int,input().split())) for _ in range(N)]
#     min_v = 9 * N
#     P = list(range(N))
#     f(0,N)



def calc(i,K):
    global min_sum
    if i == K:
        s = 0
        for j in range(K):
            s += arr[j][P[j]]
        if min_sum > s:
            min_sum = s
    else:
        for idx in range(i,K):
            P[i],P[idx] = P[idx],P[i]
            calc(i+1,K)
            P[i],P[idx] = P[idx],P[i]
    return min_sum




T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    P = list(range(N))
    min_sum = 9*N
    print(f"#{tc+1}",calc(0,N))
