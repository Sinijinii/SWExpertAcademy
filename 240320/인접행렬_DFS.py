# graph = [
#     [0, 1, 0, 1, 0],         # 0번 위치에서 갈 수 있는 곳을 저장
#     [1, 0, 1, 0, 1],
#     [0, 1, 0, 0, 0],
#     [1, 0, 0, 0, 1],
#     [0, 1, 0, 1, 0]
# ]
# visited = [0 for _ in range(5)]
# path = []
# def dfs(now):
#     # 기저 조건
#
#     # 다음 재귀 호출 전
#     visited[now] = 1
#     print(now, end=" ")
#
#     # 다음 재귀 호출
#     # dfs: 현재 노드에서 다른 노드들을 확인 > 반복문
#
#     for to in range(5):
#         # 갈 수 없다면 pass
#         if graph[now][to] == 0:
#             continue
#         # 이미 방문했다면 pass
#         if visited[to]:
#             continue
#
#         visited[to] = 1
#         path.append(to)
#         dfs(to)
#    # 돌아왔을 때 작업
#
#
# # 출발점 초기화
# visited[0] = 1
# path.append(0)
# dfs(0)
# print(path)







graph = [
    [0, 1, 0, 1, 0],         # 0번 위치에서 갈 수 있는 곳을 저장
    [1, 0, 1, 0, 1],
    [0, 1, 0, 0, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0]
]
visited = [0 for _ in range(5)]
path = []
def dfs(now):
    # 차이점 1. 갈 수 없는 곳 조건 필요 없음
    # 차이점 2. for문 작성 수정
    for to in graph[now]:
        if visited[to]:
            continue

        visited[to] = 1
        path.append(to)
        dfs(to)
   # 돌아왔을 때 작업


# 출발점 초기화
visited[0] = 1
path.append(0)
dfs(0)
print(path)