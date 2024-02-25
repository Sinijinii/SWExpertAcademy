from collections import deque
T = int(input())
for tc in range(T):
    N, P = map(int,input().split())
    piz = deque(list(map(int,input().split())))
    piz_num = {}
    piz_num_list = deque(range(1,P+1))
    for pz in range(P):
        piz_num[pz+1] = piz[pz]

    oven = deque(0 for _ in range(N))
    for i in range(N):
        if oven[i] == 0:
            oven[i] = piz_num_list.popleft()

    while len(oven) > 1 :
        if int(piz_num[oven[0]]//2) >= 1:
            piz_num[oven[0]] = int(piz_num[oven[0]]//2)
            oven.append(oven[0])
            oven.popleft()
        else:
            piz_num[oven[0]] = 0
            oven.popleft()
            if len(piz_num_list) != 0:
                oven.append(piz_num_list.popleft())
    print(f"#{tc+1}",*oven)