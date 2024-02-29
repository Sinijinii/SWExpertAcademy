def babygin(card):
    card.sort()
    result = 'x'
    for i in range(len(card)):
        if card.count(card[i]) >= 3:
            return "승"
        result_run = 0
        for j in range(1,3):
            if card.count(card[i] + j) >= 1:
                result_run += 1
        if result_run >= 2:
            return "승"
    return result

T = int(input())
for tc in range(T):
    card = list(map(int,input().split()))
    p1 = []
    p2 = []
    for i in range(0,12,2):
        p1.append(card[i])
        p2.append(card[i+1])
    result = 0
    for i in range(3,6):
        if babygin(p1[:i+1]) == "승":
            result = 1
            break
        if babygin(p2[:i+1]) == "승":
            result = 2
            break
    print(f"#{tc+1}",result)
