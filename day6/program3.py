
#with O(n) space and time complexity
def main():
    size = int(input("Enter the size of list "))
    li = []
    other = set()
  
    for _ in range(size):
        try:
            li.append(int(input("enter value ")))
        except:
            raise ValueError("please try valid input")
    for i in range(1, max(li)):
        other.add(i)
      
    print("The missing element is ", min(other - set(li)))
   
   
main()
