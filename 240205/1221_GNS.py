T = int(input())
num_idx = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for tc in range(T):
    tc_num, len_str = map(str,input().split())
    str_1 = list(input().split())
    sort_str = []
    for num in num_idx:
        for data in str_1:
            if num == data:
                sort_str.append(data)



    print(tc_num, *sort_str)
