def find_set(x):
    # 자기 자신이 대표면 끝
    if arr[x] == x:
        return x
    return find_set(arr[x])

# 3. union
def union(x,y):
     x = find_set(x)
     y = find_set(y)

     # 이미 같은 집합이라면 패스
     if x == y:
         return

     # 다른 집합이라면 합침
     if x < y:
         arr[y] = x
     else:
         arr[x] = y


T = int(input())
for tc in range(T):
    N, M = map(int,input().split())
    arr = list(i for i in range(N+1))
    groups = [ 0 for i in range(N)]
    t = list(map(int,input().split()))
    for i in range(M):
        l, r = t[i * 2], t[i * 2 + 1]
        union(l,r)

    # 1~N까지 각각 대표를 찾아줌
    for i in range(1, N + 1):
        groups[i - 1] = find_set(i)

    print(f'#{tc+1} {len(set(groups))}')