'''그림과 같이 인덱스가 있는 10x10 격자에 빨간색과 파란색을 칠하려고 한다.
N개의 영역에 대해 왼쪽 위와 오른쪽 아래 모서리 인덱스, 칠할 색상이 주어질 때, 칠이 끝난 후 색이 겹쳐 보라색이 된 칸 수를 구하는 프로그램을 만드시오.
주어진 정보에서 같은 색인 영역은 겹치지 않는다.'''

T = int(input())
for tc in range(T):
    # 10*10 격자 생성
    arr = [[0] * 10 for i in range(10)]

    N = int(input())
    # 겹친구간의 수를 구할 result
    result = 0
    for N_C in range(N):
        # 모서리 인덱스, 칠할 색상 받기
        r1,c1,r2,c2,color = map(int,input().split())
        # 색칠할 부분의 범위 구하기
        ri = r2-r1
        ci = c2-c1
        # 각 색의 숫자로 색칠
        for i in range(ri+1):
            for j in range(ci+1):
                arr[r1+i][c1+j] += color
    # 전체 격자를 돌며 겹친구간이 있는지 구함
    for i in range(10):
        for j in range(10):
            if arr[i][j] >= 3:
                result += 1
    print(f'#{tc+1} {result}')


