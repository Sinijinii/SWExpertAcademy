def dfs(y,x,path):
    # 기저 조건
    if len(path) == 7:
        # 현재까지 경로 저장
        result.add(path)
        return



T = int(input())
for tc in range(T):
    # maps = [list(map(int,input().split())) for _ in range(4)]
    maps = [input().split() for _ in range(4)]
    # 중복제거를 위한 set사용
    result = set()

    # 시작지점
    for i in range(4):
        for j in range(4):
            dfs(i,j,maps[i][j])