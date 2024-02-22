import math
T = int(input())
for tc in range(T):
    data = float(input())
    result = ""
    sum_data = 0
    for i in range(1,14):
        quotient = math.floor(data * 2)
        if (data * 2) - quotient != 0:
            data = (data * 2) - quotient
            sum_data += quotient * (2 ** -i)
            result += str(quotient)
        else:
            result += str(quotient)
            break

    if len(result) >= 13:
        result = "overflow"
    print(f"#{tc+1}",result)
