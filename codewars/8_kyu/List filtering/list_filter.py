def filter_list(l):
    n_list = []

    for items in l:
        if type(items) != str:
            print(items)
            n_list.append(items)
            
    return n_list