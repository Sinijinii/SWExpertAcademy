#import sys
#sys.stdin = open('input_view.txt','r')

T = 10
for test in range(T):
    n = int(input()) # 건물개수
    building = list(map(int, input().split()))
    sum_view = 0
    view = []
    for b_idx in range(2,len(building)-2):
        bef_buil = max([building[b_idx-2],building[b_idx-1]])
        aft_buil = max([building[b_idx+1], building[b_idx+2]])
        if building[b_idx] - bef_buil > 0 and building[b_idx] - aft_buil > 0:
            view.append(min(building[b_idx] - bef_buil, building[b_idx] - aft_buil))
    print("#{}".format(test + 1), sum(view))



