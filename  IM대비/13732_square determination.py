T = int(input())
for tc in range(T):
    N = int(input())
    arr = [input() for _ in range(N)]
    for i in range(N):
        arr[i] = arr[i].split(".")
    c = 0
    xy = []
    for i in range(N):
        for j in range(len(arr[i])):
            if "#" in arr[i][j]:
                xy.append([i,j])
    result = 0
    len_data = 0
    if xy:
        len_data = len(arr[xy[0][0]][xy[0][1]])
    for n in range(len(xy)-1):
        if arr[xy[n][0]][xy[n][1]] == arr[xy[n+1][0]][xy[n+1][1]]:
            result += 1
    if result == len_data -1 and len_data == len(xy):
        result = 'yes'
    else:
        result = 'no'
    print(f"#{tc+1}",result)