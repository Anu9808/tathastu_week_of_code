def main():
  dic_size = int(input("Enter the number of items "))
  dic = {}
  for i in range(dic_size):
      key = input("Enter the key ")
      value = int(input("Enter the value "))
      dic[key] = value
      
  final = {}
  for key,value in dic.items():
      if value not in final.values():
          final[key] = value
  print("Dictonary after removing duplicate values: ", final)
  
main()
