import textwrap

def wrap(string, max_width):
    
    string = textwrap.fill(string,max_width)
    string = string.replace(",","\n")  
    return string
