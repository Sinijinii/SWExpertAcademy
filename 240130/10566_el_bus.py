T = int(input())
for tc in range(T):
    K,N,M = map(int, input().split())
    M_data = list(map(int, input().split()))

    list_data = [0]*(N+1)

    for num in M_data:
        list_data[num] = 1

    sum_count = 0
    i = 0
    break_c = 0

    while i+K < N:
        if list_data[i+K] == 0:
            for j in range(i+K,i+1,-1):
                if list_data[j] == 1:
                    sum_count += 1
                    i = j
                    break_c += list_data[j]
                    break
            if break_c == 0:
                sum_count = 0
                break
        else:
            i = i+K
            sum_count += 1

    print("#{}".format(tc + 1), sum_count)


