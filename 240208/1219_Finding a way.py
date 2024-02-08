for _ in range(10):
    tc,E = map(int, input().split())
    arr = list(map(int,input().split()))

    A = [0]*100 # A[i] i에 인접한 도시 번호
    B = [0]*100
