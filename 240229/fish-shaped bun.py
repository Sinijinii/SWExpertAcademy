# 손님이 도착한 시간 > 오름차순
# 손님의 인덱스 +1 > 앞까지의 사람

def fish_bread():
    sold_bread = 0
    for person in customers:
        made_bread = (person // m) * k

        sold_bread += 1

        remain = made_bread - sold_bread

        if remain < 0:
            return "impossible"
    return "possible"

T = int(input())

for tc in range(T):
    n,m,k = map(int,input().split())
    customers = list(map(int,input().split()))
    customers.sort()
    result = fish_bread()
    print(f"#{tc+1}",result)