def longest(a1, a2):
    a1 = a1 + a2
    n_list = []
    
    for char in a1:
        if char not in n_list:
            n_list.append(char)
            
    result = "".join((sorted(n_list)))
    
    return result