def generate(numRows):
  pascal = [[1], [1,1]]
  
  for i in range(3, numRows+1):
    row = [1]
    for j in range(i-2):
      print(i, j)
      row.append(pascal[i-2][j] + pascal[i-2][j+1])
    row.append(1)
    pascal.append(row)
    print(pascal)
  
  return pascal

generate(5)
n = 10
print([n, 1, n+1, 0][n % 4])
print([n, 1, n+1, 0])
print([n, 1, n+1, 0][3])