def repeated(data):
    idx = "-"
    for i in range(len(data)-1):
        if data[i] == data[i+1]:
            idx = i + 1
            break
    if idx == "-":
        return len(data)
    else:
        rep_data = data[0:idx-1] + data[idx+1:]
        return repeated(rep_data)


T = int(input())
for tc in range(T):
    str_data = input()
    print(f'#{tc+1} {repeated(str_data)}')



