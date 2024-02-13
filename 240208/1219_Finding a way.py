def dfs(s,e):   # start, end
    visit = [0]*100
    stack = []
    # 시작점 방문 표시
    visit[s] = 1
    while True:
        # 현재 방문한 정점
        # 인접 도시
        w = A[v]
        if w != -1 and visit[w] == 0:
            stack.append(v)     #지나간칸을 스택에 저장
            v = w
            visit[v] = 1
        elif B[v]!=-1 and visit[B[v]] == 0:
            stack.append(v)
            v = B[v]
            visit[v] = 1
        else: #지나온 곳에서 다시 탐색
            if stack:   #지나온 곳에 남아있으면
                v = stack.pop()
            else:       # 출발지까지 거슬러와서 가능한 모든곳을 확인한 경우
                break
        if v == e:
            return 1
    return 0


for _ in range(10):
    tc,E = map(int, input().split())
    arr = list(map(int,input().split()))

    A = [0]*100 # A[i] i에 인접한 도시 번호
    B = [0]*100
    for i in range(0,E*2,2):
        n1,n2 = arr[i],arr[i+1]
        if A[n1] == -1:
            A[n1] = n2
        else:
            B[n1] = n2

    dfs(0,99)