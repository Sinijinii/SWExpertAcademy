#min,max와 그에 대한 인덱스 값을 구하는 함수
def min_max(Box_size,data):
    min_data = data[0]
    min_data_idx = 0
    max_data = data[0]
    max_data_idx = 0
    for num in range(Box_size):
        if min_data > data[num]:
            min_data_idx = num
            min_data = data[num]
        elif max_data < data[num]:
            max_data_idx = num
            max_data = data[num]
    return min_data_idx,min_data,max_data_idx,max_data
#본문
T = 10
BOX = 100

for tc in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    for tc_data in range(N):
        min_data_idx,min_data,max_data_idx,max_data = min_max(BOX,data)
        data[min_data_idx] += 1
        data[max_data_idx] -= 1
    min_data_idx,min_data,max_data_idx,max_data = min_max(BOX,data)
    print("#{}".format(tc + 1), max_data-min_data)
