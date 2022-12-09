import stack as s

st = s.Stack(10)

post_ex = '123+*4*'

for token in post_ex:
    if '0' <= token <= '9':
        st.push(float(token))
    else:
        a = st.pop()
        b = st.pop()

        if token == '+':
            st.push(b+a)
        elif token == '-':
            st.push(b-a)
        elif token == '*':
            st.push(b*a)
        elif token == '/':
            st.push(b/a)

print(st.pop())

