def solve(s):
    words = s.split(" ")


    for i in range(len(words)):

        if(len(words[i])>0 and not words[i][0].isnumeric() == True ):
            words[i] = words[i].capitalize()
        else:
            continue


    result = ' '.join(words)


    
    return result