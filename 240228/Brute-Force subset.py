arr = ['A','B','C','D','E']

N_arr = 5
result = 0
#
# for i in range(1 << N_arr):
#     sum_data = 0
#     list_data = []
#     for j in range(N_arr):
#         if i & (1 << j):
#             sum_data += 1
#     if sum_data >=2:
#         result += 1
# print(result)


def get_count(tar):
    cnt = 0
    for i in range(N_arr):
        if tar & 0x1:
            cnt +=1
        tar >>= 1
    return cnt

for tar in range(1<<N_arr):
    if get_count(tar) >= 2:
        result += 1
print(result)
