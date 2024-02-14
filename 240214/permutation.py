def f(i,k):
    if i == k:
        print(*P)
    else:
        # P[i]자리로 바꿀(올)원소 P[j]
        for j in range(i,k):
            # P[i] <->P[j]
            P[i],P[j] = P[j],P[i]
            f(i+1,k)
            P[i],P[j] = P[j],P[i] # 교환전으로 복구


N = 3
P = [1,2,3]
f(0,N)