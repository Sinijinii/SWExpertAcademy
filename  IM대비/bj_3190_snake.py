N = int(input())
K = int(input())
arr = [list(0 for _ in range(N)) for __ in range(N)]
for a in range(K):
    i,j = map(int,input().split())
    arr[i-1][j-1] = 1

L= int(input())
lo = {}
for l in range(L):
    a,b = input().split()
    lo[int(a)] = b

s_x,s_y = 0,0
di = [0,1,0,-1]
dj = [1,0,-1,0]

vis = [[0,0]]
cnt = 0
i = 0
while True:
    if cnt in lo:
        if lo[cnt] == "D":
            i += 1
        else:
            i -= 1
    if i == 4:
        i = 0
    elif i == -1:
        i = 3
    if 0<=s_x+di[i]<N and 0<=s_y+dj[i]<N and ([s_x+di[i],s_y+dj[i]] not in vis):
        cnt+=1
        s_x += di[i]
        s_y += dj[i]
        if arr[s_x][s_y] == 1:
            vis.append([s_x,s_y])
            arr[s_x][s_y] = 0
        else:
            vis.append([s_x,s_y])
            vis.pop(0)

    else:
        break
print(cnt+1)