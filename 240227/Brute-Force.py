path = []
def pmt(x,sum):
    global cnt
    if sum > 10:
        return
    if x == 3:
        print(f'{path} = {sum}')
        cnt += 1
        return
    for i in range(1,7):
        path.append(i)
        pmt(x+1,sum+i)
        path.pop()
path = []
cnt = 0
pmt(0,0)
print(cnt)
