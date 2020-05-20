def main():
    num = int(input("Enter the range"))
    a= 0
    b= 1
    print(a)
    print(b)
    for i in range(num-2):
        
        a,b = b,a+b
        print(b)
main()
