T = 10
for tc in range(T):
    len_p = int(input())
    str_arr = [input() for _ in range(8)]
    result = 0
    # 가로
    for i in range(8):
        for j in range(8-len_p+1):
            if str_arr[i][j:j+len_p] == str_arr[i][j:j+len_p][::-1]:
                result += 1
    # 세로
    for i in range(8-len_p+1):
        for j in range(8):
            str_data = ""
            for idx in range(len_p):
                str_data += str_arr[i+idx][j]
            if str_data == str_data[::-1]:
                result += 1
    print(f"#{tc+1}",result)