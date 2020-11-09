def math_operation(n1,n2,op):
    if(op=='add'):
        r=n1+n2
    if (op == 'sub'):
        r = n1 - n2
    if (op == 'mul'):
        r = n1 * n2
    if (op == 'div'):
        r = n1 / n2
    return r


output = math_operation(10,2,'add')
print(output)