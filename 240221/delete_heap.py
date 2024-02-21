# 삭제 힙
def deq(n):
    global last
    # 루트의 키값 보관
    tmp = h[1]
    h[1] = h[last]
    last -= 1
    # 새로 옮긴 루트
    p = 1
    # 왼쪽 자식
    c = p*2
    # 자식이 있으면
    while c <= last:
        # 오른쪽 자식도 있고, 왼쪽 자식보다 더 크면
        if c + 1 <= last and h[c] < h[c+1]:
            c += 1
        # 부모와 자식을 비교
        if h[p] < h[c]:
            h[p],h[c] = h[c],h[p]
            # 자식을 부모로 변경
            p = c
            c = p*2
        # 부모가 더 큰경우
        else:
            break
    return tmp

N = 10          # 필요한 노드 수
h = [0]*(N+1)   # 최대 힙
last = 0        # 힙의 마지막 노드 번호


while (last > 0):
    print(deq())