def generate_4l(input_str_4l):
    array = str(input_str_4l)
    searchstr = "ts:.+"
    r = array.count("r")
    g = array.count("g")
    b = array.count("b")
    if r != 0 :
        searchstr += r"(?=(\S*r){" +f"{r}"+"})"
    if g != 0 :
        searchstr += r"(?=(\S*g){"+f"{g}"+"})"
    if b != 0 :
        searchstr += r"(\S*b){"+f"{b}"+"}"
    if r == b == g == 0:
        searchstr = ""
    return searchstr
