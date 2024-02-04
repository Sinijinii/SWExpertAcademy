T = int(input())
for tc in range(T):
    # 배열의 크기 N, 파리채의 크기 M
    N,M = map(int, input().split())
    arr = []
    #di=[0,0,1,1,2,2] dj=[0,1,2,0,1,2,..]
    di = sum(list([i]*M for i in range(M)),[])
    dj = list(i for i in range(M))*M
    # 최종값
    result = 0
    # arr데이터 받기
    for data in range(N):
        arr.append(list(map(int, input().split())))
    # 배열 순회
    for i in range(N):
        for j in range(N):
            sum_data = 0
            for d in range(len(di)):
                ni = i + di[d]
                nj = j + dj[d]
                if 0 <= ni < N and 0 <= nj < N:
                    sum_data += arr[ni][nj]
                if sum_data > result:
                    result = sum_data
    print("#{}".format(tc + 1), result)
