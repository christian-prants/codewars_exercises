def move_zeros(lst):
    count = 0
    n_arr = []

    for x in lst:
        if x == 0:
            count += 1 

    def filter_arr(value):
        if value != 0:
            return True
        else:
            return False

    f_arr = filter(filter_arr, lst)

    for num in f_arr:
        n_arr.append(num)

    while count != 0:
        n_arr.append(0)
        count -= 1

    return n_arr