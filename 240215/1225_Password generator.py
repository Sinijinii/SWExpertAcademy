from collections import deque
T = 10
for tc in range(T):
    tc_num = int(input())
    arr = deque(map(int,input().split()))
    tf = True
    while tf:
        for i in range(1,6):
            pn = arr[0] - i
            if pn <= 0:
                pn = 0
                tf = False
                arr.append(pn)
                arr.popleft()
                break

            arr.append(pn)
            arr.popleft()
    print(f"#{tc_num}",*arr)