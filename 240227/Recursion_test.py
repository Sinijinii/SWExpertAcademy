def f(x):
    if x == 6:
        return
    print(x,end=" ")
    f(x+1)
    print(x,end=" ")
f(0)