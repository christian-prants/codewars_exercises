def find_uniq(arr):
    arr.sort()
    a_size = len(arr) - 1
    
    for index, num in enumerate(arr):
        if (index == a_size or num != arr[index + 1]) and (index == 0 or num != arr[index - 1]):
            return num
        
    return None