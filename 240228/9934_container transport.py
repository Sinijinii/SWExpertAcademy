def weight_judgment(w,tr):
    global cnt
    st_tr = 0
    st_w = 0
    len_tr = len(tr)
    if len(tr) == 0:
        return
    for i in range(len(w)):
        if tr[st_tr] >= w[st_w]:
            cnt += w[st_w]
            tr.pop(st_tr)
            w.pop(st_w)
            break
        else:
            st_w += 1
    if len_tr == len(tr):
        tr.pop(0)
    weight_judgment(w,tr)

T = int(input())
for tc in range(T):
    N,M = map(int,input().split())
    w = list(map(int,input().split()))
    tr = list(map(int,input().split()))
    w.sort(reverse=True)
    tr.sort()
    result = 0
    cnt = 0
    weight_judgment(w,tr)
    print(f"#{tc+1}",cnt)
