def stealing(house_val, k): # k represents number of houses
	if k == 0: 
		return 0
	if k == 1: 
		return house_val[0] 
	value2 = max(house_val[0], house_val[1]) 
	if k == 2: 
		return value2
	value1 = house_val[0]
	for i in range(2, k): 
		max_val = max(house_val[i]+value1, value2) 
		value1 = value2 
		value2 = max_val 

	return max_val 

def main():

  n = int(input("Enter number of houses: "))
  house_val = []
  for i in range(n):
      house_val.append(int(input("House " + str(i+1) + " : ")))

  print("Maximum possible stolen value :", stealing(house_val, n)) 
  
main()
