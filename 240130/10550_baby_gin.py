# T = int(input())
# for tc in range(T):
#     data = str(input())
#     data_list = []
#     for list in data:
#         data_list.append(int(list))
#     data_list.sort()
#     data_list_1_avg = sum(data_list[:3])/len(data_list[:3])
#     data_list_2_avg = sum(data_list[3:])/len(data_list[3:])
#     if len(set(data_list)) != 3:
#         if data_list_1_avg == data_list[1] and (data_list[1]-data_list[0] == 1 or data_list[1]==data_list[0]):
#             if data_list_2_avg == data_list[4] and (data_list[4]-data_list[3] == 1 or data_list[4]==data_list[3]):
#                 print("#{}".format(tc + 1), 'Baby Gin')
#             else: print("#{}".format(tc + 1), 'Lose')
#         else: print("#{}".format(tc + 1), 'Lose')
#     else: print(list(set(data_list)))

T = int(input())
for tc in range(T):
    data = int(input())
    c = [0]*12
    for i in range(6):
        c[data%10] += 1
        data //= 10

    i = 0
    tri = run = 0
    while i<10:
        if c[i] >= 3:
            c[i] -= 3
            tri += 1
            continue
        if c[i] >= 1 and c[i+1] and c[i+2]>=1:
            c[i] -= 1
            c[i+1] -= 1
            c[i+2] -= 1
            run += 1
            continue
        i += 1
    if run + tri ==2: print("#{}".format(tc + 1),"Baby Gin")
    else: print("#{}".format(tc + 1),'Lose')