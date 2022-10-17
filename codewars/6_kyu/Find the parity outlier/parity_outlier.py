def find_outlier(integers):
    odds = [ number % 2 for number in integers ]

    if odds.count(0) == 1:          
        return integers[odds.index(0)]    
    else:         
        return integers[odds.index(1)]