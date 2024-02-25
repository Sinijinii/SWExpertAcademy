from collections import deque
T = 10
for tc in range(T):
    tc_num = int(input())
    arr = deque(list(map(int,input().split())))
    while arr[-1] > 0:
        for c in range(1,6):
            arr.append(arr[0]-c)
            arr.popleft()
            if arr[-1] <= 0:
                arr[-1] = 0
                break
    print(f"#{tc+1}",*arr)