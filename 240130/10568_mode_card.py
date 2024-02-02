T = int(input())
for tc in range(T):
    N = int(input())
    data = str(input())
    data_count_list = []
    for i in data:
        data_num = 0
        for j in data:
            if i == j:
                data_num += 1
        data_count_list.append(data_num)
    max_list = list(filter(lambda x: data_count_list[x] == max(data_count_list), range(len(data_count_list))))
    max_data = 0
    max_idx = 0
    for max_ in max_list:
        if max_data < int(data[max_]):
            max_data = int(data[max_])
            max_idx = data_count_list[max_]
    print("#{}".format(tc + 1), int(max_data),max_idx)
