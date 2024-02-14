def f(i,k,t): #k개의 원소를 가진 배열 A에서 부분집합의 합이 t인 경우
    global result
    count = 0
    # 모든 원소에 대해 포함(결정)하면
    if i == k:
        ss = 0  # 부분집합의 합
        for j in range(k):
            # 0인경우 외에는 다 참이기에
            # bit[j] == 1
            if bit[j]:  #A[j]가 포함된 경우
                ss += arr[j]
        if ss == t:
            count = 0
            for j in range(k):
                # 0인경우 외에는 다 참이기에
                # bit[j] == 1
                if bit[j]:  # A[j]가 포함된 경우
                    count += 1
        if count == N:
            result += 1
    else:
        for j in range(1,-1,-1):
            bit[i] = j
            f(i+1,k,t)
        # bit[i] = 1
        # f(i+1,k)
        # bit[i] = 0
        # f(i+1, k)
    return result

T = int(input())
for tc in range(T):
    N,K = map(int, input().split())
    arr = [1,2,3,4,5,6,7,8,9,10,11,12]
    bit = [0]*len(arr)
    result = 0
    print(f'#{tc+1}', f(0,12,K))