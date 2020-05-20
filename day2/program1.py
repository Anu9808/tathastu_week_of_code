def palindrome(num):
    rem, sum_ = 0, 0
    num_copy = num
    while num_copy > 0:
        rem = num_copy % 10
        sum_ = sum_*10+rem
        num_copy = num_copy // 10
    if sum_ == num:
        return True
    else:
        return False
def armstrong(num):
    rem, sum_ = 0, 0
    len_= len(str(num))
    num_copy = num
    while num_copy > 0:
        rem = num_copy % 10
        sum_ = sum_+rem**len_
        num_copy = num_copy // 10
    if sum_ == num:
        return True
    else:
        return False
   
def check_prime(num):
  i=2
  while i*i<=num:
    if num%i == 0:
      return False
    i+=1
  return True
  
def even_or_odd(num):
  if num % 2 ==0:
    print("Even Number")
  else:
    print("Odd Number")
    
def main():
  num = int(input("Enter the number"))
  if even_or_odd(num):
    print("The number is even")
  else:
    print("The number is odd")
    
  if check_prime(num):
    print("The number is Prime")
  else:
    print("The number is Not Prime")
    
  if armstrong(num):
    print("The number is armstrong number")
  else:
    print("The number is not armstrong")
          
  if palindrome(num):
    print("The number is palindrome")
  else:
    print("The number is not palindrome")
          
main()
