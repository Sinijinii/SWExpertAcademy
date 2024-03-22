V,E = map(int,input().split())

# 우선 순위 큐를 활용
from heapq import heappush,heappop

def prim(start):
    pq = []
    vis = [0] * V

    # 최소 비용
    sum_weight = 0

    # 시작점 추가
    # [기존 BFS] 노드 번호만 관리
    # [Prim] 가중치가 낮으면 먼저 나와야 함
    # -> 관리해야할 데이터 : 가중치, 노드번호 2가지
    # -> 동시에 두가지 데이터를 다루는 방법
        # 1. class로 만들기 (3가지 이상일땐 Class)
        # 2. 튜플로 관리
    # 이차원 배열 + 가중치 + 높이
    heappush(pq, (0,start))
    while pq:
        weight , now = heappop(pq)

        # 우선 순위 큐의 특성상
        # 더 먼거리로 가는 방법이 큐에 저장이 되어 있기 때문에
        # 기존에 이미 더 짧은 거리로 방문했다면 continue
        # 방문을 했다면 continue
        if vis[now]:
            continue

        # 방문 처리
        vis[now] = 1
        # 누적합 추가
        sum_weight += weight

        # 갈 수 있는 노드들을 보면서
        for to in range(V):
            # 갈 수 없거나 이미 방문했다면 pass
            if graph[now][to] == 0 or vis[to]:
                continue

            heappush(pq, (graph[now][to], to))
    print("최소 비용", sum_weight)


# 인접 행렬로 저장
# 실습 - 인접 리스트로 저장
graph = [[0] * V for _ in range(V)]
for _ in range(E):
    s,e,w = map(int,input().split())

    # [기존] 3 > 4로 갈 수 있다.
    # graph[3][4] = 1

    # [가중치 그래프] 3 > 4 로 가는데 31이라는 비용이 든다.
    graph[s][e] = w
    graph[e][s] = w     # 무방향 그래프
prim(0)