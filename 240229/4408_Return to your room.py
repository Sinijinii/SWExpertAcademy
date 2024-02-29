T = int(input())
for tc in range(T):
    N = int(input())
    corridor = [0]*400 # 복도 리스트 초기화
    max_v = 0

    for i in range(N):
        s,e = map(int,input().split())
        # 아랫방을 윗방으로 변경
        if s % 2 == 0:
            s -= 1
        if e % 2 == 0:
            e -= 1
        # 출발지보다 목적지 값이 더 큰값이 되도록 swap
        if s > e:
            s,e = e,s
        for i in range(s,e+1):
            corridor[i] += 1
            max_v = max(corridor[i],max_v)
    print(f"#{tc+1}",max_v)
