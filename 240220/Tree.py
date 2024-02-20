'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

# 전위순회
def pre_order(T):
    if T:
        print(T,end=" ")
        pre_order(left[T])
        pre_order(right[T])




N = int(input())
E = N - 1
arr = list(map(int, input().split()))
left = [0] * (N+1)          # 부모를 인덱스로 왼쪽자식 번호 저장
right = [0] * (N+1)
par = [0] * (N+1)           #자식을 인덱스로 부모 저장

for i in range(E):
    p,c = arr[i*2],arr[i*2+1]
# for i in range(0,E*2,2):
#    p,c = arr[i], arr[i+1]
    if left[p]==0:
        left[p] = c
    else:
        right[p] = c
    par[c] = p
print(par)
print(left)
print(right)

c = N
while par[c] != 0:
    print(c)
    print(par[c])
    c = par[c]
# print(c)
root = c

pre_order(root)