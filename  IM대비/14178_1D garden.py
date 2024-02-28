T = int(input())
for tc in range(T):
    N,D = map(int,input().split())
    # 분무기의 개수 > 꽃의 개수 // 물을 줄수 있는 범위 + 나머지가 있다면 1
    spr = N //((D*2)+1)
    if N % ((D*2)+1) != 0:
        spr += 1
    print(f"#{tc+1}",spr)