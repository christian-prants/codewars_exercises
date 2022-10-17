def number(bus_stops):
    in_outs = 0
    result = 0
    
    for people in bus_stops:
        in_outs = people[0] - people[1]
        result += in_outs
        
    return result