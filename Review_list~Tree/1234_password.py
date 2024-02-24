T = 10
for tc in range(T):
    N,pw = input().split()
    i = 1
    while i < len(pw):
        if pw[i] == pw[i-1]:
            pw = pw[:i-1] + pw[i+1:]
            i = 1
        else:
            i += 1
    print(f"#{tc+1}",pw)