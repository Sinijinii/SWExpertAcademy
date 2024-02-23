# T = int(input())
# for tc in range(T):
#     N,M = map(int,input().split())
#     binary = bin(M)
#     bin_num = binary[2:]
#     result = 'ON'
#     for i in range(1,N+1):
#         if bin_num[-i] == '1':
#             pass
#         else:
#             result = 'OFF'
#             break
#     print(f"#{tc+1}",result)



#2
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    temp = M
    for i in range(N):
        if temp & 0x1 == 0:
            print(f"#{tc} OFF")
            break
        temp = temp >> 1
    else:
        print(f"#{tc} ON")


#3
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    #bit(N-1) - bit0 이 모두 1인 숫자
    # N = 4인 경우 > 00001111 = 10000 - 1 = (1<<4) -1
    b = (1<<N) - 1
    #print(f"{b:b}")
    # &연산자의 경우 모두가 1일때만 1, 아니라면 0 이 출력됨
    if M & b == b:
        print(f"#{tc} ON")
    else:
        print(f"#{tc} OFF")
