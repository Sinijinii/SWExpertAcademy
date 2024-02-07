# 스택 구현해보기
top = -1
stack =[0]*10
size = 10
def push(n,size):
    global top
    top += 1
    if top == size:
        print('overflow')
    else :
        stack[top] = n

push(10,10)
push(20,10)
push(30,10)
push(40,10)

while top >= 0:
    top -= 1
    print(stack[top+1])