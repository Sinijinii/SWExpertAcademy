def post(arr):
    st = []
    result = ""
    for i in arr:
        if i in "+-*/":
            while st and op.get(st[-1], 0) >= op.get(i, 0):
                result += st.pop()
            st.append(i)
        else:
            result += i
    while len(st) > 0:
        result += st.pop()
    return result

def calc(post):
    post = list(post)
    i = 1
    while len(post) > 1:
        if post[i] in "*+-/":
            if post[i] == "*":
                post[i] = str(int(post[i-2]) * int(post[i-1]))
                post.pop(i-2)
                post.pop(i-2)
                i = 1
            elif post[i] == "/":
                post[i] = int(int(post[i-2]) // int(post[i-1]))
                post.pop(i-2)
                post.pop(i - 2)
                i = 1
            elif post[i] == "+":
                post[i] = int(post[i-2]) + int(post[i-1])
                post.pop(i-2)
                post.pop(i - 2)
                i = 1
            elif post[i] == "-":
                post[i] = int(post[i-2]) - int(post[i-1])
                post.pop(i-2)
                post.pop(i - 2)
                i = 1
        else:
            i += 1
    return post
op = {"+": 1, "-": 1, "*": 2, "/": 2}
T = 10
for tc in range(T):
    N = int(input())
    arr = input()
    print(f"#{tc+1}",*calc(post(arr)))


