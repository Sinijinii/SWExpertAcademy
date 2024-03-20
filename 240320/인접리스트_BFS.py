# 2. 인접 리스트
graph = [
    [1, 3],
    [0, 2, 4],
    [1],
    [0, 4],
    [1, 3]
]
visited = [0 for _ in range(5)]
def bfs(start):

    # 시작 노드를 큐에 추가 + 방문 표시
    Q = [start]
    visited[start] = 1

    while Q:
        now = Q.pop(0)
        print(now, end=' ')

        # 갈 수 있는 곳을 체크
        for to in graph[now]:
            if visited[to]:
                continue

            visited[to] = 1
            Q.append(to)

bfs(0)
