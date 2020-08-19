def evalRPN(tokens):
    stack = []
    for i in tokens:
        try:
            if i.isdigit() or int(i)<0:
                stack.append(i)
        except:
            v1 = stack.pop()
            v2 = stack.pop()
            if(i == '/' or i == '-'):
                print(v2+i+v1)
                stack.append(str(int(float(eval(v2+i+v1)))))
            else:
                print(v1+i+v2)
                stack.append(str(eval(v1+i+v2)))
        print("stack:")
        print(*stack,sep = ',')
    return int(float(stack.pop()))
expr1 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
value=evalRPN(expr1)
print('the result of postfix expression:'+str(value))
