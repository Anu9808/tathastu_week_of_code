
def main():
    
    num = int(input("Enter number "))
    print("Entered number",num)
    num_new = int(str(num).replace('0','5'))
    print("Number after replacing '0' with '5' is: ", num_new)
main()
