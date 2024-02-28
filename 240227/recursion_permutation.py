# def pmt(x):
#     if x == 3:
#         print(pmt_list)
#         return
#     for i in range(6):
#         pmt_list.append(i+1)
#         pmt(x+1)
#         pmt_list.pop()
#
#
# pmt_list = []
#
# pmt(0)



def pmt(x):
    if x == 2:
        print(pmt_list)
        return
    for i in range(6):
        if used[i] == True:      # 추가: 이미 사용한 숫자인지 여부 확인
            continue
        used[i] = True           # 처음 사용이라면 숫자를 기록
        pmt_list.append(i+1)
        pmt(x+1)
        pmt_list.pop()
        used[i] = False          # 모든 처리가 끝나고 돌아온 후 기록 지움


pmt_list = []
used = [0,0,0,0,0,0]
pmt(0)