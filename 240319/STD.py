# 순열
def dfs_permutation(level):
    # 기저조건
    # 이 문제에서는 3개를 뽑았을때까지 반복
    if level == 3:
        print(*vis)
        return

    # 들어가기 전
    # 다음 재귀 호출
    # - 다음에 갈 수 있는 곳들은 어디인가?
    # - 이 문제에서는 1,2,3 세가지 경우(arr의 길이만큼)가 존재

    # 기본 코드
    # vis[level] = 1
    # dfs(level + 1)
    #
    # vis[level] = 2
    # dfs(level + 1)
    #
    # vis[level] = 3
    # dfs(level + 1)

    for i in range(len(arr)):

        if arr[i] in vis:
            continue
        vis[level] = arr[i]
        dfs_permutation(level + 1)

        vis[level] = 0







def dfs(level):
    # 기저조건
    # 이 문제에서는 3개를 뽑았을때까지 반복
    if level == 3:
        print(*vis)
        return

    # 들어가기 전
    # 다음 재귀 호출
    # - 다음에 갈 수 있는 곳들은 어디인가?
    # - 이 문제에서는 1,2,3 세가지 경우(arr의 길이만큼)가 존재

    # 기본 코드
    # vis[level] = 1
    # dfs(level + 1)
    #
    # vis[level] = 2
    # dfs(level + 1)
    #
    # vis[level] = 3
    # dfs(level + 1)

    for i in range(len(arr)):
        vis[level] = arr[i]
        dfs(level + 1)

arr = [i for i in range(1,4)]
vis = [0] * 3
# dfs(0)
print("-----------------------")
vis = [0] * 3
dfs_permutation(0)