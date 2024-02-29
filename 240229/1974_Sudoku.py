def sudoku(arr):
    for i in range(9):
        L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        W = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        result = 0
        for j in range(9):
            if arr[i][j] in L:
                L.remove(arr[i][j])
            else:
                return result
            if arr[j][i] in W:
                W.remove(arr[j][i])
            else:
                return result

    for x in range(0,9,3):
        for y in range(0,9,3):
            N = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for i in range(3):
                for j in range(3):
                    if arr[x+i][y+j] in N:
                        N.remove(arr[x+i][y+j])
                    else:
                        return result
    return 1


T = int(input())
for tc in range(T):
    arr = [list(map(int,input().split())) for _ in range(9)]
    print(f"#{tc+1}",sudoku(arr))