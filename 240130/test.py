T = int(input())
for tc in range(T):
    data = int(input())
    c = [0]*12
    for i in range(6):
        c[data%10] += 1
        data //= 10

    i = 0
    tri = run = 0
    while i<10:
        if c[i] >= 3:
            c[i] -= 3
            tri += 1
            continue
        if c[i] >= 1 and c[i+1] and c[i+2]>=1:
            c[i] -= 1
            c[i+1] -= 1
            c[i+2] -= 1
            run += 1
            continue
        i += 1
    if run + tri ==2: print("#{}".format(tc + 1),"Baby Gin")
    else: print("#{}".format(tc + 1),'Lose')