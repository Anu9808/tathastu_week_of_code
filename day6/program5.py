def main():
    
    fib = set()
    f,s = 0,1
    fib.add(f)
    fib.add(s)
    for i in range(50):
        k = f+s
        fib.add(k)
        f,s=s,k
        
        
    size = int(input("\nEnter your list size:"))
    li = list()
    fib_sum = 0
    for i in range(size):
        elem=int(input("Enter element {}:".format(i+1)))
        li.append(elem)
        if elem in fib:
            fib_sum+=elem

    print("Given sequence:",li)
    print("Sum of fibonnaci elements is:",fib_sum)

    if(fib_sum in fib):
        print("{} is a Fibonnaci Number".format(fib_sum))

    else:
        print("{} is not a Fibonnaci Number".format(fib_sum))
   

main()
