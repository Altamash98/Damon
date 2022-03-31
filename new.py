import sys
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)

if __name__ == "__main__":
    num = sys.argv[1:]
    for n in num:
        n = int(n)
        factorial = fact(n)
        print(f"the factorial of numbers {n} is {factorial}")


