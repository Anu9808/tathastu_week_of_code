def main():
    size = int(input("Enter size of list: "))
    li = []
    
    for i in range(size):
         li.append(int(input("Enter element " + str(i+1) + " "))) 
    
    li.sort()
    
    print("\n Possible Largest product of 3 numbers in list is ", li[-1]*li[-2]*li[-3])
    
main()
