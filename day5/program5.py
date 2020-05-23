def even_odd(lis):
    odd_li = []
    even_li = []
    for e in lis:
        if e%2 == 0:
            even_li.append(e)
        else:
            odd_li.append(e)
    return sorted(odd_li, reverse = True) + sorted(even_li)

def main():

    num = int(input("Enter the size of the list : "))
    lis = []
    for i in range(num):
        lis.append(int(input("Enter element "+str(i+1)+" : ")))
    print("The sorted list is as follows : ",even_odd(lis))
    
main()
