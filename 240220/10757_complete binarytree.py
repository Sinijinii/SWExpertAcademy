
def in_order(T,N):
    global cnt
    if T <= N:
        in_order(T*2,N)# 왼쪽 자식 노드 방문
        tree[T] = cnt
        cnt+=1
        in_order(T*2+1,N) # 오른쪽 자식 노드 방문

T = int(input())
for tc in range(T):
    N = int(input())
    tree = [0] * (N + 1)  # 비어있는 완전이진트리
    cnt = 1
    in_order(1, N)
    print(f'#{tc+1} {tree[1]} {tree[N // 2]}')



