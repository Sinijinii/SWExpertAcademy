T = int(input()) # 테스트 케이스 개수 T
for tc in range(T):
    N = int(input()) # 삼각형의 크기
    # 0이 담긴 이중리스트 생성 > [[0],[0,0],[0,0,0],....]
    arr = list([0] * i for i in range(1,N+1))
    # 각 행의 양쪽 끝은 1로 채워짐 > [[1],[1,1],[1,0,1],[1,0,0,1],...]
    for i in range(N):
        arr[i][0],arr[i][-1] = 1,1
    # 왼쪽 위, 오른쪽 위의 합을 해당 인덱스에 할당
    # ex) 1,0과 1,1의 좌표를 2,1에 할당 / 2,0과 2,1좌표를 3,1에...
    for i in range(1,N-1):
        for j in range(0,i):
            arr[i+1][j+1] = arr[i][j] + arr[i][j+1]
    # 결과 출력
    print(f'#{tc+1}')
    for i in arr:
        print(*i)

