stone_c = {0:1,1:0}
T = int(input())
for tc in range(T):
    N,M = map(int,input().split())
    stone = list(map(int,input().split()))
    for num in range(M):
        i,j = map(int,input().split())
        for st in range(1,j+1):
            idx = i-1
            if 0 <= idx+st < N and 0<= idx-st < N:
                if stone[idx+st] == stone[idx-st]:
                    stone[idx+st] = stone_c[stone[idx+st]]
                    stone[idx - st] = stone_c[stone[idx - st]]
    print(f"#{tc+1}",*stone)