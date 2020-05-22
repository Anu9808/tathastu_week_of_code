def main():
  list_size = int(input("Enter the no of tuples in the list "))
  tuple_size= int(input("Enter the no. of elements in each tuple "))
  list_ = []
  for _ in range(list_size):
      print("Enter the elements in tuple", _ + 1)
      tup = []
      for j in range(tuple_size):
          tup.append(int(input("Enter element space")))
      list_.append(tuple(tup))
      
  index = int(input("Enter the nth index about which you want to sort the list: "))
  list_.sort(key = lambda x : x[index])
  print("Sorted tuples List by nth index sort:",list_)
  
main()
