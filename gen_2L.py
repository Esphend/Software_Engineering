def generate_2L(input_str_2l):
    array = input_str_2l.split()
    searchstr = ""
    enternum = 0
    for element in array:
        if enternum != 0:
            searchstr += "|"
        if element[1] == element[0]:
            searchstr += element[1] + "-" + element[0]
        else:
            searchstr += element[0] + "-" + element[1] + "|" + element[1] + "-" + element[0]
        enternum += 1
    return searchstr
