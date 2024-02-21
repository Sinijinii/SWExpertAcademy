
T = int(input())
for tc in range(T):
    # 노드의 개수 N과 리프 노드의 개수 M, 값을 출력할 노드 번호 L
    N,M,L= map(int,input().split())
    leaf = [list(map(int,input().split())) for _ in range(M)]
    h = [0] * (N + 1)  # 비어있는 완전이진트리
    for data in range(M):
        leaf_n = leaf[data][0]
        leaf_v = leaf[data][1]
        h[leaf_n] = leaf_v


    c = N
    p = c // 2
    # print("c :",c)
    # print("p :",p)
    # 왼쪽
    if c % 2 == 0:
        # 부모의 값을 왼쪽으로 두기 / 오른쪽 값이 없을 경우가 있기에 왼쪽으로 해둬야힘
        h[p] = h[c]
        # 오른쪽 값을 가기 위해
        c -= 1
    # 오른쪽일 경우
    while c > 0:
        # 부모는 자식의 1/2
        p = c // 2
        # 부모위치에 왼쪽 자식값과, 오른쪽 자식의 값을 더해줌
        h[p] = h[c] + h[c - 1]
        c -= 2
    print(f'#{tc+1} {h[L]}')