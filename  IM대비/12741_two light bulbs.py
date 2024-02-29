T = int(input())
result = []
for tc in range(T):
    A,B,C,D = map(int,input().split())
    on = [A,C]
    off = [B,D]
    if min(off)-max(on) > 0:
        result.append(min(off)-max(on))
    else:
        result.append(0)
for i in range(T):
    print(f"#{i+1}",result[i])
