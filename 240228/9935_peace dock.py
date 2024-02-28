def f(s,e):
    global result
    cnt = 1
    if s == e:
        return
    st = s
    for i in range(s,N-1):
        if arr[st][1] <= arr[i+1][0]:
            st = i+1
            cnt += 1
    if result < cnt:
        result = cnt
    f(s+1,e)
T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    arr.sort(key = lambda x : x[1], reverse=False)
    result = 0
    f(0,24)
    print(f"#{tc+1}",result)