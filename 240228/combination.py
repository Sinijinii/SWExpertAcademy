# 5명중 n명을 뽑는 코드
arr = ['A','B','C','D','E']
path = []

n = 3
def combination(lev,start):
    if lev == n:
        print(path)
        return
    for i in range(start,5):
        path.append(arr[i])
        combination(lev+1, i+1)
        path.pop()

combination(0,0)

# 중복 조합
arr = [1,2,3,4,5,6]
path = []

n = 3
def combination(lev,start):
    if lev == n:
        print(path)
        return
    for i in range(start,6):
        path.append(arr[i])
        combination(lev+1, i)
        path.pop()

combination(0,0)