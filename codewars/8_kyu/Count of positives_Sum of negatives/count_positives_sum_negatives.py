def count_positives_sum_negatives(arr):
    positive = 0
    negative = 0
    
    if len(arr) != 0:
        for p in arr:
            if p > 0:              
                positive = positive + 1
            
        for n in arr:
            if n < 0:
                negative = negative + n
                
        final = [positive, negative]
    else:
        final = []
    
    return final