def main():
    size = int(input("Enter number of strings: "))
    ls = []
    
    for i in range(size):
         ls.append(str(input("Enter string " + str(i+1) + " : "))) 
        
    ls.sort(key = lambda i : len(i))
    print(ls)

    n1 = len(ls[0]) 
    n2 = len(ls[size-1]) 
          
    result = "" 
          
    j = 0
    i = 0
    while(i <= n1 - 1 and j <= n2 - 1): 
        if (ls[0][i] != ls[size-1][j]): 
            break
        result += (ls[0][i]) 
        i += 1
        j += 1
    
    print("Longest common prefix:", result)
