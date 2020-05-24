def main():
  size = int(input("Enter the size of list "))
  li = []
  for _ in range(size):
      
    li.append(int(input("enter value ")))
  li.sort()
  print("list after sorting ", li)
   
   
main()
