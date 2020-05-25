def main():

    n = int(input("Enter size of array: "))
    arr = []

    for i in range(n):
        arr.append(int(input("Enter value"))) 

    for i in range(1,n-1):
        if max(arr[:i]) < arr[i] < min(arr[i+1:]):
            print(arr[i])
            break
    else:
        print("Not Found")
        
main()
