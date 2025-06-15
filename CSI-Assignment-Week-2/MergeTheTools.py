def merge_the_tools(string, k):
    
    for i in range(0, len(string), k):
        
        t = string[i:i+k]   
        seen = set()
        result = []
        
        for ch in t:
            if ch not in seen:
                seen.add(ch)
                result.append(ch)
                
        print(''.join(result))