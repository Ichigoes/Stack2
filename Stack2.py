expression = input()
s = []

for i in range(len(expression)):
    ch = expression[i]
    if ch == "(":
        s.append(i)
    elif ch == ")":
        start_index = s.pop()
        end_index = i + 1
        print(expression[start_index:end_index])
