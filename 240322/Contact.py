# 자료구조 : 그래프(인접행렬, 인접리스트)
# 알고리즘: BFS

def bfs(start):
    q = [start]
    vis = [0] * (101)
    vis[start] = 1
    # 가장 깊은 depth의 가장 큰 수
    max_number = start
    # 가장 깊은 depth
    max_depth = 1
    while q:
        now = q.pop(0)
        # 갈 수 있는 곳들
        for to in graph[now]:
            if vis[to]:
                continue
            # 현재 방문 = 이전방문 + 1
            vis[to] = vis[now] + 1
            # 최대 깊이에 따라 값 변경
            if max_depth < vis[to] or (max_depth == vis[to] and max_number < to):
                max_depth = vis[to]
                max_number = to
            q.append(to)
    return max_number

T = 10
for tc in range(T):
    N,start = map(int,input().split())
    input_graph = list(map(int,input().split()))
    # 인접리스트
    graph = [[] for _ in range(101)]
    for i in range(0,N,2):
        s = input_graph[i]
        e = input_graph[i+1]
        graph[s].append(e)

    print(f"#{tc+1}",bfs(start))
