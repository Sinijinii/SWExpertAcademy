a2 = ['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']
a16 = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
T = int(input())
for tc in range(T):
    num, data = input().split()
    result = ""
    for i in range(int(num)):
        idx = a16.index(data[i].lower())
        result += a2[idx]
    print(f"#{tc+1}",result)