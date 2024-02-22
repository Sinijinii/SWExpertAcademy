T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int,input().split()))
    result = []
    cr_sum = 1
    for idx in range(1,len(arr)):
        if arr[idx] > arr[idx-1]:
            cr_sum += 1
        else:
            result.append(cr_sum)
            cr_sum = 1
    result.append(cr_sum)
    print(f"#{tc+1}",max(result))