T = int(input())
for tc in range(T):
    N = int(input())
    data = list(map(int,input().split()))
    data_mode = []
    for mode in data:
        data_num = 0
        for mode_in in data:
            if mode == mode_in:
                data_num += 1
        data_mode.append(data_num)
    mode_idx = data_mode.index(max(data_mode))
    print("#{}".format(tc + 1), data[mode_idx])
