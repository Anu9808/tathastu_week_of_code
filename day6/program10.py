def main():
    
    li_size = int(input("Enter the list size "))
    ele_size = int(input("Enter the size of list "))
    
    main = []       #list of list
    for i in range(li_size):
        li=[]
        for j in range(ele_size):
            li.append(int(input("Enter {} element in {} list".format(j+1,i+1))))
        main.append(li)   
        
    new = [] #extended list
    for i in main:
        i.sort()
        new.extend(i)
    new.sort()
    print("The new extended list",new)
   
main()
