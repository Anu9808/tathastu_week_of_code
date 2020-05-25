def ack(m,n):
    if m==0:
        return n+1
    if n==0:
        return ackerman(m-1,1)
    
    n2 = ackerman(m,n-1)
    return ackerman(m-1,n2)

def main():
    a = int(input("first value"))
    b = int(input("second value"))
    print("\nThe computed ackerman value is:", ackerman(a,b))
    
main()
