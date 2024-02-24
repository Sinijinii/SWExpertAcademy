code = [[3,2,1,1],[2,2,2,1],[2,1,2,2],[1,4,1,1],[1,1,3,2],[1,2,3,1],[1,1,1,4],[1,3,1,2],[1,2,1,3],[3,1,1,2]]
code_f = [[2,1,1],[2,2,1],[1,2,2],[4,1,1],[1,3,2],[2,3,1],[1,1,4],[3,1,2],[2,1,3],[1,1,2]]
a2 = ['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']
a16 = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']

T = int(input())
for tc in range(T):
    N,M = map(int,input().split())
    arr = [input() for _ in range(N)]
    binary_arr = []
    sum_arr = []
    for i in range(N):
        binary = ""
        for j in range(M):
            binary += a2[a16.index(arr[i][j].lower())]
        binary_arr.append(binary)

    cnt = []
    for x in range(N):
        idx = 0
        cnt_str = []
        for y in range(1,len(binary_arr[x])):
            if binary_arr[x][y-1] != binary_arr[x][y]:
                cnt_str.append(y-idx)
                idx = y
        cnt.append(cnt_str)
    print(cnt)




    cnt_f = cnt[0]
    num = 1
    result1 = []

    for cnt_num in range(1,len(cnt)):

        if cnt_f == cnt[cnt_num]:
            num += 1
            cnt_f = cnt[cnt_num]
        else:
            num = 1
            cnt_f = cnt[cnt_num]
        if num >= 5:
            if len(result1) == 0 or(len(result1) > 0 and result1[-1] != cnt[cnt_num]):

                result1.append(cnt[cnt_num])

    result1 = list(filter(None, result1))
    print(result1)
    result = []
    for i in range(len(result1)):
        idx = 0
        for _ in range(int(len(result1[i])/32)):
            result.append(result1[i][idx:idx+32])
        idx += 32
    result = list(set(map(tuple,result)))
    fin_result = 0
    for r in range(len(result)):
        idx_re = 0
        number = ""
        for r1 in range(8):
            arr_f = result[r][idx_re:idx_re+4]
            if r1 == 0:
                arr_f = result[r][idx_re + 1:idx_re+4]
                number += str(code_f.index(list(map(lambda x: int(x/min(arr_f)), arr_f))))
            else:
                number += str(code.index(list(map(lambda x: int(x/min(arr_f)), arr_f))))
            idx_re += 4

        even = 0
        odd = 0
        for i in range(8):
            if i % 2 == 0:
                even += int(str(number[i]))
            else:
                odd += int(str(number[i]))

        if (even * 3 + odd) % 10 == 0:
            fin_result += sum(list(map(int, list(number))))
        else:
            pass

    print(f"#{tc+1}",fin_result)



