T = int(input())

for num in range(T):
    data_len, sum_num = map(int,input().split())
    data = list(map(int, input().split()))
    sum_min = sum(data[:sum_num])
    sum_max = sum(data[:sum_num])
    sum_data = 0
    for idx in range(data_len-sum_num+1):
        last_idx = idx + sum_num
        sum_data = sum(data[idx:last_idx])
        if sum_data > sum_max:
            sum_max = sum_data
        elif sum_data < sum_min:
            sum_min = sum_data
    print("#{}".format(num + 1), sum_max-sum_min)