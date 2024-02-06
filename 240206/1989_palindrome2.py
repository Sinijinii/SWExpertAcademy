T = int(input())

for tc in range(T):
    str_data = input()
    N_str = len(str_data)
    num = N_str // 2
    s_cnt = 0
    result = 0
    for i in range(num):
        if str_data[i] == str_data[-(i+1)]:
            s_cnt += 1
    if s_cnt == num:
        result = 1
    print(f'#{tc+1} {result}')
