numTerms = int(input("Fibonacci numbers to print"))

def fibonacci(n):
    if n<=1:
        return n
    else: 
        return(fibonacci(n-1)+fibonacci(n-2))
    

if numTerms <= 0:
    print("Please enter a positive number")
else:
    print("Fibonacci sequence:")
    for i in range(numTerms):
        print(fibonacci(i))
