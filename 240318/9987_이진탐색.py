def bsearch(key,n):
    dir = 0 # 1-왼쪽 선택, 2-오른쪽 선택
    l = 0
    r = n-1
    # 구간이 반복할 때의 리턴값, 반복하지 않으면 0
    result = 1
    # 검색 구간이 존재하면
    while l <= r:
        m = (l+r)//2
        # 검색에 성공한 경우
        if A[m] == key:
            # 검색에 성공하고, result가 1인 경우
            return result
        elif A[m] > key:
            r = m-1
            # 이전에도 왼쪽을 선택한 경우
            if dir == 1:
                result = 0
            dir = 1
        else:
            l = m+1
            if dir == 2:
                result = 0
            dir = 2
    return 0

T = int(input())
for tc in range(T):
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    A.sort()
    cnt = 0
    for k in B:
        cnt += bsearch(k,N)
    print(f'#{tc+1}',cnt)