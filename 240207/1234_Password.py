##
def repeated(data):
    idx = "-"
    for i in range(len(data)-1):
        if data[i] == data[i+1]:
            idx = i + 1
            break
    if idx == "-":
        return data
    else:
        rep_data = data[0:idx-1] + data[idx+1:]
        return repeated(rep_data)


T = 10
for tc in range(T):
    N_data, str_data = map(str,input().split())
    print(f'#{tc+1} {repeated(str_data)}')
