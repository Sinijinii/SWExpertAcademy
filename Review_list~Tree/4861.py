T = int(input())
for tc in range(T):
    N,M = map(int, input().split())
    str_arr = [list(input()) for _ in range(N)]
    result = ""
    # 가로
    for i in range(N):
        for j in range(N-M+1):
            # 가로
            if str_arr[i][j:j+M] == str_arr[i][j:j+M][::-1]:
                result += "".join(map(str,str_arr[i][j:j+M]))

    # 세로
    for i in range(N-M+1):
        for j in range(N):
            str_data = ""
            for idx in range(M):
                str_data+=str_arr[i+idx][j]
            if str_data == str_data[::-1]:
                result = str_data


    print(f"#{tc+1}",result)