# 1. Write python program for a recursive routine to find the sum of all the even numbers between 0 and n when called with an even number. Show how the subroutine would be called and the result output.
# 2. Write an python program to print the first n Fibonacci sequence without recursion
# 3. Write an python program to print the first n Fibonacci sequence using recursion

# 1.
def SumNum(n):
  if n == 0:
    return 0
  else:
    return n + SumNum(n-2)
# Main
n=int(input("Enter any even number: \n"))
SumNum(n)

# 2.
def 