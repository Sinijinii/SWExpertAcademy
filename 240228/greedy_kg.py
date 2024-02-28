n = 3
target = 30
things = [(5,50),(10,60),(20,140)] # kg, price
things.sort(key = lambda x : (x[1]/x[0]), reverse=True)

result = 0

for kg,price in things:
    per_price = price/kg
    # 만약 가방에 남아있는 용량이 얼마 안된다면, 문건을 잘라서 가방에 넣고 끝
    if target <kg:
        result += target * per_price
        break
    result += price
    target -= kg

print(int(result))
