T = int(input())
for tc in range(T):
    x1,y1,x2,y2 = list(map(int,input().split()))
    cx1,cy1,cx2,cy2 = list(map(int,input().split()))
    result = 1
    if x2 < cx1 or y2 < cy1 or cx2<x1 or cy2<y1:
        result = 4
    if (x1 == cx2 and y1 == cy2) or (x2 == cx1 and y1 == cy2) or (x2 == cx1 and y2 == cy1) or (x1 == cx2 and y2 == cy1):
        result = 3
    elif (x1 == cx2) or (x2 == cx1) or (y2 == cy1) or (y1 == cy2):
        result = 2
    print(f"#{tc+1}",result)