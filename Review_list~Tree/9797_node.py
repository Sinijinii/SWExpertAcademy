def Queue(S):
    visited[S] = 1
    Q = []
    Q.append(S)
    print(adjl)
    cnt = 0
    while Q:
        S = Q.pop()
        for n in adjl[S]:
            if visited[n] == 0:
                visited[n] = cnt+1
                Q.append(n)
                S = n
                cnt += 1
                break

        print(visited)
    print()


T = int(input())
for tc in range(T):
    V,E = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(E)]
    S,G = map(int,input().split())
    visited = [0] * (V+1)
    adjl = [[] for _ in range(V+1)]
    for i in range(E):
        adjl[arr[i][0]].append(arr[i][1])
        adjl[arr[i][1]].append(arr[i][0])
    Queue(S)
