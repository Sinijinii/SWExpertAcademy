N,M = map(int,input().split())
s_x,s_y, l = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
vis = [(s_x,s_y)]
#북 동 남 서(0,1,2,3)
di = [-1,0,1,0]
dj = [0,1,0,-1]
# 북쪽일때는 > 0 서 남 동 북 (3 2 1 0)
# 동쪽일때는 > 1 북 서 남 동 (0 3 2 1)
# 남쪽일때는 > 2 동 북 서 남 (1 0 3 2)
# 서쪽일때는 > 3 남 동 북 서 (2 1 0 3)
# ==(현재 위치 + 3) % 4
while True:
    x,y = vis.pop(0)
    arr[x][y] = 2
    for i in range(4):
        idx = (l+3)%4
        if arr[x+di[idx]][y+dj[idx]] == 0:
            l = idx
            arr[x + di[idx]][y + dj[idx]] = 2
            vis.append((x+di[idx],y+dj[idx]))
            break
        else:
            l = idx
    else:
        if l == 1:
            if arr[x+di[3]][y+dj[3]] != 1:
                vis.append((x+di[3],y+dj[3]))
            else:
                break
        else:
            if arr[x+di[abs(l-2)]][y+dj[abs(l-2)]] != 1 :
                vis.append((x+di[abs(l-2)],y+dj[abs(l-2)]))
            else:
                break
res = 0
for i in range(N):
    res += arr[i].count(2)
print(res)
