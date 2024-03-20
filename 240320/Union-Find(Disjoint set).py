# 1~6까지 노드가 존재
# 1. make-set
def make_set(n):
    return [i for i in range(n)]

# 2.find_set
# 부모노드를 보고, 부모 노드도 연결이 되어 있다면 다시 반복
# 자기 자신이 대표인 데이터를 찾을 때 까지 반복
parents = make_set(7)
def find_set(x):
    # 자기 자신이 대표면 끝
    if parents[x] == x:
        return x
    return find_set(parents[x])


# 3. union
def union(x,y):
     x = find_set(x)
     y = find_set(y)

     # 이미 같은 집합이라면 패스
     if x == y:
         return

     # 다른 집합이라면 합침
     if x < y:
         parents[y] = x
     else:
         parents[x] = y

union(1,3)
union(2, 3)
union(5,6)
print(parents)