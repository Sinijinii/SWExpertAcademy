T = int(input())
for tc in range(T):
    arr = list(input())
    i = 0
    j = 0
    result = ""
    for idx in range(7,71,7):
        data = arr[i:idx]
        sum_data = 0
        for j in range(7):
            if data[6-j] == "1":
                sum_data += 2**j
        i = idx
        result = result + str(sum_data) + " "
    print(f"#{tc+1}",result)


