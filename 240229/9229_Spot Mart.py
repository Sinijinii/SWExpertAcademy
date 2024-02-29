T = int(input())
for tc in range(T):
    N,M = map(int,input().split())
    arr = list(map(int,input().split()))

    result = -1
    for i in range(1<<N):
        cnt = 0
        sum_w = 0
        for j in range(N):
            if i & (1<<j):
                cnt += 1
                sum_w += arr[j]
        if cnt == 2 and sum_w <= M:
            if result<sum_w:
                result = sum_w
    print(f"#{tc+1}",result)