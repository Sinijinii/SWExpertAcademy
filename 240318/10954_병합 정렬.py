def merge_sort(arr):
    global cnt
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)
    if left[-1] > right[-1]:
        cnt += 1
    return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int,input().split()))
    cnt = 0
    print(f'#{tc+1}',merge_sort(arr)[N//2],cnt)