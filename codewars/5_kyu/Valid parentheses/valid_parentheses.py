def valid_parentheses(string):
    list_01 = ['(', '[', '{']
    list_02 = [')', ']', '}']
    stack = []

    for prts in string:              
        if prts in list_01:
            stack.append(prts)
        elif prts in list_02:
            try:
                stack.pop()
            except:
                return False
                
    if len(stack) == 0:
        return True
    else:
        return False