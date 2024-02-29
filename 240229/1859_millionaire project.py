def max_mon(arr):
    global count
    max_m = max(arr)
    max_idx = arr.index(max_m)
    if max_idx == len(arr)-1 or max_idx == 0:
        if max_idx != 0:
            max_data = arr[max_idx]
            data = arr[:max_idx]
            # print(count)
            # print((max_data * len(data)) - sum(data))
            count += (max_data * len(data)) - sum(data)
            return count
        return count
    else:
        data = arr[:max_idx]
        count += (arr[max_idx] * len(data)) - sum(data)
        max_mon(arr[max_idx+1 :])

T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int,input().split()))
    count = 0
    max_mon(arr)
    print(f"#{tc+1}",count)
    # print(f"#{tc+1}",max_mon(arr))