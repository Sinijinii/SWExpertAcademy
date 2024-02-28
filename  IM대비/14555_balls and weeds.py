balls = ["(",")"]
T = int(input())
for tc in range(T):
    S = input()
    count = 0
    for i in S:
        if i in balls:
            count += 1
    b_S = len(S)
    S = S.replace("()","")
    a_S = len(S)
    com_ball_num = (b_S - a_S)//2
    count -= com_ball_num


    print(f"#{tc+1}",count)