def spiral(arr,m,n) : 
	k = 0; l = 0

	while (k < m and l < n) :  
		for i in range(l, n) : 
			print(arr[k][i], end = " ") 
		k += 1

		for i in range(k, m) : 
			print(arr[i][n - 1], end = " ") 
		n -= 1

		if ( k < m) : 
			for i in range(n - 1, (l - 1), -1) : 
				print(arr[m - 1][i], end = " ") 
			m -= 1
		
		if (l < n) : 
			for i in range(m - 1, k - 1, -1) : 
				print(arr[i][l], end = " ") 
			l += 1

    
    
    
def main():
    
    row = int(input("Enter row count "))
    col = int(input("Enter column count "))    
    mat=[]

    for i in range(row):
        print("\nEnter values in row {}:".format(i+1))

        co=[]
        for j in range(col):
            co.append(int(input("Enter value in column {}:".format(j+1))))
        mat.append(co)

    print("\nThe input matrix is:")
    for i in range(row):
        print(mat[i])

    print("\nThe spiral output is:\n")
    spiral(mat,row,col)
    
main()
