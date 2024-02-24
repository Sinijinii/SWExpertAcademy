T = int(input())
arr = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for tc in range(T):
    num, str_len = input().split()
    str = input().split()
    idx = 0
    result = []
    while idx < 10:
        n = arr[idx]
        for i in str:
            if n == i:
                result.append(i)
        idx += 1
    print(num,*result)
