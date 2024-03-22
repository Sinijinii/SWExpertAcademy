def dsf(st,sum_data):
    global res
    if sum_data >= B and res > (sum_data-B):
        res = (sum_data-B)
        return
    if st < N:
        dsf(st+1,sum_data+arr[st])
        dsf(st+1, sum_data)

T = int(input())
for tc in range(T):
    N,B = map(int,input().split())
    arr = list(map(int,input().split()))
    res = 1e9
    dsf(0,0)

    print(f"#{tc+1}",res)