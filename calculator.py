 # x = float(input("What's x?"))
 # y = float(input("What's y?"))  
 # int(x) makes turns the number into an acutal number to the pc
 # z = int(x) + int(y)
 # z = round(x + y)
 # z = round(x / y, 2)
 # print (z)
 # print(f"{z:.2f}")
 #float is a number with a decimal point by changing int() to float()
 #x = int(input("What's x?"))
 # y = int(input("What's y?"))  
 # round(number[, ndigits])

# number squared calculator
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n


main()
