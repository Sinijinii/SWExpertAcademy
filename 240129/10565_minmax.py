num = int(input())
for i in range(num):
    num_data = int(input())
    data = list(map(int,input().split()))
    min_data = data[0]
    max_data = data[0]
    for j in data:
        if j > max_data:
            max_data = j
        elif j < min_data:
            min_data = j

    print("#{}".format(i + 1), max_data-min_data)