T = int(input())
for tc in range(T):
    str_data = input()
    i = 1
    while i < len(str_data):
        # print(i, str_data)
        if str_data[i-1] == str_data[i]:
            str_data = str_data[0:i-1]+str_data[i+1:]
            i=1
        else:
            i+=1
    print(f"#{tc+1}",len(str_data))