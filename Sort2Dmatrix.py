# Python3 code to sort 2D matrix row-wise
def sortRowWise(m):
     
    # loop for rows of matrix
    for i in range(len(m)):
         
        # loop for column of matrix
        for j in range(len(m[i])):
             
            # loop for comparison and swapping
            for k in range(len(m[i]) - j - 1):
                 
                if (m[i][k] > m[i][k + 1]):
                     
                    # swapping of elements
                    t = m[i][k]
                    m[i][k] = m[i][k + 1]
                    m[i][k + 1] = t
                     
    # printing the sorted matrix
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end=" ")
        print()
 
# Driver code
m = [[9, 8, 7, 1 ],[7, 3, 0, 2],[9, 5, 3, 2],[ 6, 3, 1, 2 ]]
sortRowWise(m)
 
