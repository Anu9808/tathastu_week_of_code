def knapsack(bag, wt, val, n): 

  ''' count the maximum possible value things that can be fit in knapsack bag.'''
  
    if n == 0 or W == 0 : 
        return 0
    if (wt[n-1] > W): 
        return knapsack(W, wt, val, n-1) 
    else: 
        return max( val[n-1] + knapsack(W-wt[n-1], wt, val, n-1), knapsack(W, wt, val, n-1)) 
        
        
def main():
  n = int(input("Enter number of items "))
  val = list()
  wt = list()
  for i in range(n):
      val.append(int(input("Enter value of item " + str(i+1) + " : ")))
      wt.append(int(input("Enter weight of item " + str(i+1) + " : ")))
  bag = int(input("Enter size of knapsack: "))

  print("Total value of knapsack :", knapsack(bag, wt, val, n)) 
  
main()
