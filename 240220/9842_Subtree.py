# 전위순회
def pre_order(T):
    global result
    if T:
        result += 1
        pre_order(left[T])
        pre_order(right[T])

T = int(input())
for tc in range(T):
    E,N = map(int,input().split())
    arr = list(map(int,input().split()))
    num = E+1
    left = [0] * (num + 1)  # 부모를 인덱스로 왼쪽자식 번호 저장
    right = [0] * (num + 1)
    par = [0] * (num + 1) # 자식을 인덱스로 부모 저장
    result = 0
    for i in range(num-1):
        p,c = arr[i*2],arr[i*2+1]
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c
        par[c] = p
    pre_order(N)
    print(f"#{tc+1}",result)