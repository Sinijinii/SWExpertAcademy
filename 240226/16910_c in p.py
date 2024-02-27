def get_count(N):
    cnt = 0
    for y in range(-N,N+1):
        for x in range(-N,N+1):
            ans = x**2 + y ** 2
            if ans <= N **2:
                cnt += 1
    return cnt

T = int(input())
for tc in range(T):
    N = int(input())
    print(get_count(N))