def solution(number):
    result = 0
    
    for n in range(1, number):
        if n % 3 == 0 or n % 5 == 0:
            result = result + n
    
    return result