def main():
  dic_size = int(input("Enter the number of items "))
  dic = {}
  for i in range(dic_size):
      key = input("Enter the key ")
      value = int(input("Enter the value "))
      dic[key] = value
  print(sorted(dic.values(),reverse =True)[1])

main()
