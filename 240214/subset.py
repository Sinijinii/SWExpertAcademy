def f(i,k,t): #k개의 원소를 가진 배열 A에서 부분집합의 합이 t인 경우
    # 모든 원소에 대해 포함(결정)하면
    if i == k:
        ss = 0  # 부분집합의 합
        for j in range(k):
            # 0인경우 외에는 다 참이기에
            # bit[j] == 1
            if bit[j]:  #A[j]가 포함된 경우
                ss += A[j]
        if ss == t:
            for j in range(k):
                # 0인경우 외에는 다 참이기에
                # bit[j] == 1
                if bit[j]:  # A[j]가 포함된 경우
                    print(A[j],end=" ")
            print()
    else:
        for j in range(1,-1,-1):
            bit[i] = j
            f(i+1,k,t)
        # bit[i] = 1
        # f(i+1,k)
        # bit[i] = 0
        # f(i+1, k)

N = 10
A = [1,2,3,4,5,6,7,8,9,10]
# bit[i]는 A[i]가 부분집합에 포함되는지 표시
bit = [0]*N
f(0,N,10)



# 두번째 버전
# def f(i,k,s,t): #k개의 원소를 가진 배열 A에서 부분집합의 합이 t인 경우
#     global cnt
#     cnt += 1
#     # 모든 원소에 대해 포함(결정)하면
#     if s == t:
#         for j in range(k):
#             if bit[j]:  #A[j]가 포함된 경우
#                 print(A[j],end = " ")
#         print()
#     elif i == k: # 모든 원소를 고려했으나 s!=t
#         return
#     elif s > t:
#         return
#
#     else:
#         bit[i] = 1
#         f(i+1,k,s+A[i],t)
#         bit[i] = 0
#         f(i+1, k,s, t)
#
# N = 10
# A = [1,2,3,4,5,6,7,8,9,10]
# # bit[i]는 A[i]가 부분집합에 포함되는지 표시
# bit = [0]*N
# cnt = 0
# f(0,N,0,5)
# print("cnt: ",cnt)