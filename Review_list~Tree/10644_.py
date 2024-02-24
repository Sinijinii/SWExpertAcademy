T = int(input())
for tc in range(T):
    str1 = input()
    str2 = input()
    result = 0
    for i in str1:
        cnt = 0
        for j in str2:
            if i == j:
                cnt += 1
        if result < cnt:
            result = cnt
    print(f"#{tc+1}",result)