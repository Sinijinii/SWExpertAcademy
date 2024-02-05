T = int(input())
for tc in range(T):
    str1 = input()
    str2 = input()
    result = 0
    for i in str1:
        count_data = 0
        for j in str2:
            if i == j:
                count_data += 1
        if count_data > result:
            result = count_data
    print(f'#{tc+1} {result}')