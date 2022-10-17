import itertools

def get_pins(observed):
    adjacent_dict = {
        "1" : ['1','2','4'],
        "2" : ['1','2','3','5'],
        "3" : ['2','3','6'],
        "4" : ['1','4','5','7'],
        "5" : ['2','4','5','6','8'],
        "6" : ['3','5','6','9'],
        "7" : ['4','7','8'],
        "8" : ['5','7','8','9','0'],
        "9" : ['6','8','9'],
        "0" : ['0','8']
    }
    
    n_list = []

    for num in observed:
        n_list.append(adjacent_dict[num])    
        
    f_list = list(itertools.product(*n_list))    

    return [''.join(x) for x in f_list]