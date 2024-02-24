T = int(input())
for tc in range(T):
    N,K = map(int,input().split())
    result = 0
    arr = list(range(1,13))
    for i in range(1<<12):
        cnt = 0
        sum_sub = []
        for j in range(12):
            if i & 1<<j:
                cnt += 1
                sum_sub.append(arr[j])
        if cnt == N and sum(sum_sub) == K:
            result += 1
    print(f"#{tc+1}",result)
