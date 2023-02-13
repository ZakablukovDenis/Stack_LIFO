value = input('Введите строку: ')

stack = []
Verify_flag = True

for bracket in value:
    
    if bracket in '([{':
        stack.append(bracket)
    elif bracket in ')]}':

        if len(stack) == 0:
            Verify_flag = False
            break

        last_bracket = stack.pop()

        if last_bracket == '(' and bracket == ')':
            continue
        if last_bracket == '[' and bracket == ']':
            continue
        if last_bracket == '{' and bracket == '}':
            continue

        Verify_flag = False
        break
        
if Verify_flag and len(stack) == 0:
    print('Сбалансированно')
else:
    print('Несбалансированно')
