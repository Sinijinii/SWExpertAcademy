N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
island = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            island.append([i,j])
print(island)