# find_set
def find_set(x):
    # 자기 자신이 대표면 끝
    if parents[x] == x:
        return x
    return find_set(parents[x])

# union
def union(x,y):
     x = find_set(x)
     y = find_set(y)

     # 이미 같은 집합이라면 패스
     if x == y:
         return

     # 다른 집합이라면 합침
     if x < y:
         parents[y] = x
     else:
         parents[x] = y


T = int(input())
for tc in range(T):
    N,M = map(int,input().split())
    parents = list(range(N+1))
    for i in range(M):
        x,y = map(int,input().split())
        union(x,y)
    res = []
    for j in range(1,N+1):
        res.append(find_set(j))
    print(f"#{tc+1}", len(set(res)))

