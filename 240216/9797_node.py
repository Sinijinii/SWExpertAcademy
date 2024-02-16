def bfs(s,N,G): #시작정점 s, 노드개수N
    # 큐
    q  =[]
    # visited
    visited = [0]*(N+1)
    # 시작점 인큐
    q.append(s)
    # 시작점 방문표시
    visited[s] = 1
    # 큐가 비워질때까지
    while q:
        t = q.pop(0)
        if t == G:
            return visited[t] -1

        for i in adjl[t]:
            # 방문하지 않은 정점이면 방문 표시
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1 + visited[t]
    return 0 # 경로가 없는 경우



T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    #arr = list(map(int, input().split()))
    # 인접리스트
    adjl = [[] for _ in range(V+1)]
    for i in range(E):
        n1,n2 = map(int,input().split())
        adjl[n1].append(n2)
        adjl[n2].append(n1) #무향그래프
    S,G = map(int, input().split())

    print(f"#{tc+1}", bfs(S,V,G))