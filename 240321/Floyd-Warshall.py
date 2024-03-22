# Floyd
n = int(input()) # 노드의 수
m = int(input()) # 간선의 수
map_info = [[987654321]*(n+1) for _ in range(n+1)]
# 일단 무한대로 이루어진 arr 생성
for i in range(n+1):
    for j in range(n+1):
        if i == j:
            map_info[i][j] = 0
# 자기 자신으로 가는 값들은 0으로 변경

for _ in range(m):
    from_a, to_b, cost = map(int, input().split())
    map_info[from_a][to_b] = cost
# 초기 거리 정보를 arr에 입력

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            map_info[a][b] = min(map_info[a][b], map_info[a][k] + map_info[k][b])
# 정보를 갱신한다. (a에서 b로 한번에 가는게 더 작냐, k를 거쳐 가는 것이 더 작냐)

for a in range(1,n+1):
    for b in range(1,n+1):
        if map_info[a][b] == 987654321:
            print("INF")
        else:
            print(map_info[a][b], end = ' ') # a에서 b로 가는 경우 비용
    print()