
def calc(a, b, c='+'):
    if c == '+':
        x = a + b
    elif c == '-':
        x = a - b
    elif c == '/':
        x = a / b
    elif c == '*':
        x = a * b
    else:
       x = "I do not understand what you mean."
    return x

print calc(2,5)
print calc(3,4)
print calc(5,2,'/')
