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
#SumNum(n)

# 2.
def FibWORec():
  a=int(input("Enter the first number of desired series: \n"))
  b=int(input("Enter the second number of desired series: \n"))
  x=int(input("Enter the number of terms needed: \n"))
  while(x-2):
    c=a+b
    a=b
    b=c
    print(c,end=" ")
    x=x-1


# 3.
#def FibWRec():


# Extra: Worksheet 5 - Recursion Task 2
# Calculate and print the sequence of n Fibonacci numbers, where n is between 3 and 30.
import time
# a)
def fib(n):
  if n <= 1:
    return n
  else:
    return fib(n-1) + fib(n-2)

def fibonacci2(n):
    fibNumbers = [0,1]  #list of first two Fibonacci numbers
	# now append the sum of the two previous numbers to the list    
    for i = 2 to n:
        fibNumbers.append(fibNumbers[i-1] + fibNumbers[i-2])
	      next i
	return fibNumbers[n] 


