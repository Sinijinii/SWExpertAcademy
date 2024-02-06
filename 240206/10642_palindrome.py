T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    r = M // 2
    if M % 2 != 0:
        r2 = M // 2
    else:
        r2 = M // 2 - 1
    chr_list = [input() for _ in range(N)]
    result = ''
    for k in range(N):
        for i in range(N - M + 1):
            temp_str = ''
            temp_str2 = ''
            for j in range(i, i + M):
                temp_str += chr_list[k][j]
                temp_str2 += chr_list[j][k]
            if temp_str[:r] == temp_str[:r2:-1]:
                result = temp_str
                break
            if temp_str2[:r] == temp_str2[:r2:-1]:
                result = temp_str2
                break
        if result:
            break

    print(f'#{tc + 1} {result}')