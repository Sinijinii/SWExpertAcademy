T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(N):
            sum_data = 0
            for idx in range(N):
                sum_data += arr[idx][j]
                sum_data += arr[i][idx]
            sum_data -= arr[i][j]
            if result < sum_data:
                result = sum_data
    print(f"#{tc+1}",result)