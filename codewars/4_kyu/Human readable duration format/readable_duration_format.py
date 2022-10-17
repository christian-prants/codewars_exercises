def format_duration(seconds):
    if seconds == 0:
        return 'now'

    dict_format = {
        "year" : 60 * 60 * 24 * 365,
        "day" : 60 * 60 * 24,
        "hour" : 60 * 60,
        "minute" : 60,
        "second" : 1
    }
    date_format = {}
    format_date = ''
    s_copy = seconds

    for x in dict_format:
        date_format[x] = seconds // dict_format[x]
        format_date += "{}{} {}{}".format('' 
                                            if seconds == s_copy else ' and ' 
                                            if seconds % dict_format[x] == 0 else ', ', date_format[x], x,'s' 
                                            if date_format[x] > 1 else ''
                                        ) if date_format[x] > 0 else ''       
        seconds %= dict_format[x]

    return format_date