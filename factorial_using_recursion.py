class Factorial:
    def __init__(self, n):
        self.n = n
    
    def fact(self):
        if self.n ==0 or self.n == 1:
            return 1
        else:
            return self.n * Factorial(self.n - 1).fact()
        
if __name__ == "__main__":
    n = int(input("Enter a number to calculate its factorial: "))
    if n < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        factorial = Factorial(n)
        answer = factorial.fact()
        print(f"The factorial of {n} is: {answer}")
