# 최대힙
def enq(n):
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
    while p >= 1 and h[p] < h[c]:
        # 교환
        h[p],h[c] = h[c],h[p]
        c = p
        p = c//2
N = 10          # 필요한 노드 수
h = [0]*(N+1)   # 최대 힙
last = 0        # 힙의 마지막 노드 번호

enq(2)
print()
enq(5)

