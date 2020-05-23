def main():
    size = int(input("Enter the size of array"))
    li = [int(input("Enter element "+str(i+1) )) for i in range(size)]
    print(li)
    for i in range(len(li)-1):
        li[i] = max(li[i+1:])
    print(li)

main()
