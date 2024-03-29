'''
V E : V 1~V번까지 V개의 정점, E개의 간선
E개의 간선 정보
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def bfs(s,N): #시작정점 s, 노드개수N
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
        # t에서 할일...
        print(t)
        for i in adjl[t]:
            # 방문하지 않은 정점이면 방문 표시
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1 + visited[t]
    print(visited)


V, E = map(int, input().split())
arr = list(map(int, input().split()))

# 인접리스트
adjl = [[] for _ in range(V+1)]
for i in range(E):
    n1,n2 = arr[i*2], arr[i*2+1]
    adjl[n1].append(n2)
    adjl[n2].append(n1) #무향그래프

bfs(1,V)
