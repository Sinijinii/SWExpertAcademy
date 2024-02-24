T = int(input())
p = {'{':'}', "(":")"}
for tc in range(T):
    str_data = input()
    st = []
    result = "-"
    for i in str_data:
        if i in p:
            st.append(p[i])
        if i in p.values():
            if len(st)!=0 and i == st[-1]:
                st.pop()
            else:
                result = 0
                break

    if len(st) == 0 and result == "-":
        result = 1
    else:
        result = 0
    print(f"#{tc+1}",result)