T = int(input())
for tc in range(T):
    n = int(input())
    data = list(map(int, input().split()))
    min_data = min(data)
    max_data = max(data)
    min_data_idx = list(filter(lambda x: data[x] == min_data, range(len(data))))
    max_data_idx = list(filter(lambda x: data[x] == max_data, range(len(data))))
    print("#{}".format(tc + 1), abs(min_data_idx[0]-max_data_idx[-1]))
    list_data = [1,2,3]

