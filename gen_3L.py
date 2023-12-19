def generate_3l(input_str_3l):
    element = input_str_3l
    searchstr = ""
    enternum = 0
    if enternum != 0:
        searchstr += "|"
    if element[0] == element[1] == element[2]:                                          
        searchstr += element[0] + "-" + element[1] + "-" + element[2]
        searchstr += "|"
    if element[0] != element[1] and element[0] != element[2] and element[1] != element[2]: 
        searchstr += r'([^w])-(?!\1|w)(.)(-.)*-(?!\1|\2|w)(.)'
        searchstr += "|"
    if not (element[0] == element[1] == element[2]):
            if element[0] == element[1]:                           
                    searchstr += element[0] + "-" + element[0] + "-" + element[2] + "|"
                    searchstr += element[0] + "-" + element[2] + "-" + element[0] + "|"
                    searchstr += element[2] + "-" + element[0] + "-" + element[0] + "|"
            if element[0] == element[2]:                         
                    searchstr += element[0] + "-" + element[0] + "-" + element[1] + "|"
                    searchstr += element[0] + "-" + element[1] + "-" + element[0] + "|"
                    searchstr += element[1] + "-" + element[0] + "-" + element[0] + "|"

            if element[1] == element[2]:                        
                    searchstr += element[1] + "-" + element[1] + "-" + element[0] + "|"
                    searchstr += element[1] + "-" + element[0] + "-" + element[1] + "|"
                    searchstr += element[0] + "-" + element[1] + "-" + element[1] + "|"
    enternum += 1
    searchstr = searchstr[:-1]
    return (searchstr)
