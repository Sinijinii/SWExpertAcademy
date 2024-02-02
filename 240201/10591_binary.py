

T = int(input())
for tc in range(T):
    P,A,B = map(int,input().split())
    arr = list(range(1,P+1))
    start_a, start_b = 1, 1
    end_a, end_b = P, P
    while start_a < end_a or start_b < end_b:
        ca = int((start_a + end_a) / 2)
        cb = int((start_b + end_b) / 2)
        if arr[ca-1] == A and arr[cb-1] == B:
            print('0')
            break
        elif arr[ca-1] == A:
            print("A")
            break
        elif arr[cb-1] == B:
            print("B")
            break
        if arr[ca-1] > A:
            end_a = ca - 1
        elif arr[ca-1] < A:
            start_a = ca + 1

        if arr[cb-1] > B:
            end_b = cb - 1
        elif arr[cb-1] < B:
            start_b = cb + 1
