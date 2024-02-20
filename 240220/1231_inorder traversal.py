def in_order(T):
    global result
    if T:
        in_order(left[T])
        result += arr[T-1][1]
        in_order(right[T])

T = 10
for tc in range(T):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    E = N-1
    result = ""
    left = [0] * (N + 1)  # 부모를 인덱스로 왼쪽자식 번호 저장
    right = [0] * (N + 1)
    par = [0] * (N + 1)  # 자식을 인덱스로 부모 저장
    for i in range(N):
        pr,pl, r, l = 0, 0, 0, 0
        if len(arr[i])>=3:
            r = int(arr[i][2])
            pl = int(arr[i][0])
            if len(arr[i]) == 4:
                l = int(arr[i][3])
                pr = int(arr[i][0])

        if left[i+1] == 0:
            left[i+1] = r
        if right[i+1] == 0:
            right[i+1] = l

        if par[left[i+1]] == 0:
            par[left[i+1]] = pl
        if par[right[i+1]] == 0:
            par[right[i+1]] = pr

    c = N
    while par[c] != 0:
        c = par[c]
    root = c

    in_order(root)
    print(f"#{tc+1}",result)