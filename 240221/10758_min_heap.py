# 최소힙
def min_heap(n):
    global last
    # 마지막 노드 추가(완전이진트리 유지)
    last+=1
    # 마지막 노드에 데이터 삽입
    h[last] = n
    # 부모 > 자식 비교를 위해
    c = last
    # 부모 번호 계산
    p = c //2
    # 부모가 존재하고, 그 값이 자식보다 작다면
    while p >= 1 and h[p] > h[c]:
        # 교환
        h[p],h[c] = h[c],h[p]
        c = p
        p = c//2

# 마지막 노드의 조상 노드의 합
def node_sum(n):
     result = 0
     while n > 1:
         n = n //2
         result += h[n]
     return result

T = int(input())
for tc in range(T):
    N = int(input())         # 필요한 노드 수
    data = list(map(int,input().split()))
    h = [0]*(N+1)   # 최대 힙
    last = 0        # 힙의 마지막 노드 번호

    for i in data:
        min_heap(i)
    print(f"#{tc+1}",node_sum(N))
    #node_sum(N)
