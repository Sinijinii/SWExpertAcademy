# 갈 수 있는 곳 다가기
# 방문 순서대로 다음 노드
# 먼저 방문 -> 먼저 다음 노드
graph = [
    [0, 1, 0, 1, 0],         # 0번 위치에서 갈 수 있는 곳을 저장
    [1, 0, 1, 0, 1],
    [0, 1, 0, 0, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0]
]

def bfs(start):
    visited = [0 for _ in range(5)]

    # 시작 노드를 큐에 추가 + 방문 표시
    Q = [start]
    visited[start] = 1

    while Q:
        now = Q.pop(0)
        print(now, end=' ')

        # 갈 수 있는 곳을 체크
        for to in range(5):
            if graph[now][to] == 0:
                continue

            if visited[to]:
                continue

            visited[to] = 1
            Q.append(to)

bfs(0)
