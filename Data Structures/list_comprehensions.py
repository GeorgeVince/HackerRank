if __name__ == '__main__':
    x = 2
    y = 2
    z = 2
    n = 2

    print ([[i, j, k] for i in range(x+1) 
					  for j in range(y+1) 
					  for k in range(z+1)
					  if (i + j + k) != n])
