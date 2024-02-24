T = int(input())
for tc in range(T):
    str_data = input()
    result = 0
    if str_data == str_data[::-1]:
        result = 1
    print(f"#{tc+1}",result)