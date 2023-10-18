#factorial of a no. using Recursion
def fact(m):
  if m <= 1:
    return 1
  else:
    return m * fact(m - 1)


#main program
n = int(input("Enter the value n:"))
print("The factorial of", n, "is", fact(n))
