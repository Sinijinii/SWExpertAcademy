'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
# 시작 i, 마지막 V
def dfs(i,V):
    # visited, stack 생성 및 초기화
    visited = [0]*(V+1)
    st = []
    visited[i] = 1  # 시작점 방문
    print(i)        # 정점에서 할 일
    while True:
        # 현재 방문한 정점에 인접하고 방문안한 정점W가 있다면
        for w in adjl[i]:
            if visited[w] == 0:
                st.append(i)    #push(i), i를 지나서
                i = w           #w에 방문
                visited[i] = 1  # 방문해서 할일
                print(i)
                break
        else:                   #i에 남은 인접 정점이 없으면
            # 스택이 비어있지 않으면 (지나온 정점이 남아있다면)
            if st:
                i = st.pop()
            else: #스택이 비어있으면(출발점에서 남은 정점이 없으면)
                break #while true

V, E = map(int, input().split())
arr = list(map(int, input().split()))
# 인접리스트
# adjl[i] 행에 i에 인접인 정점 번호
adjl = [[] for _ in range(V+1)]
for i in range(E):
    n1,n2 = arr[i*2],arr[i*2+1]
    adjl[n1].append(n2)
    adjl[n2].append(n1)
dfs(1,V)