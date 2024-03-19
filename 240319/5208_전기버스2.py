def bus(idx):
    global res
    if arr[idx] + idx >= N-1:
        return
    r = 0
    max_v = 0
    for i in range(1,arr[idx]+1):
        if max_v <= arr[idx+i] + idx+i:
            max_v = arr[idx+i]+ idx+i
            r = idx + i

    res+=1
    bus(r)


T = int(input())
for tc in range(T):
    data = list(map(int,input().split()))
    N = data[0]
    arr = data[1:]
    res = 0
    bus(0)
    print(f"#{tc+1}",res)