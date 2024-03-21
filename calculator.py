try:
    a = int(input("enter 1st number : "))
    b = int(input("enter 2nd number : "))
    c = input("enter operator : ")

    if c == "+" :
        print("sum of ", a, "+", b, "=", a + b)

    elif c == "-" :
        print("subtraction of ", a,"-", b, "=", a - b)

    elif c == "*" :
        print("multiply of ", a , "*", b , "=" , a * b)

    elif c == "/" :
        print("divide of ", a , "/", b , "=" , a / b)

    elif c == "//" :
        print("floor division of ", a, "//", b , "=" , a // b)

    elif c == "**" :
        print("exponentiation of ", a, "**", b , "=" , a ** b)

    elif c == "%" :
        print("modulus of ", a, "%", b , "=" , a % b)
    else:
        print("invalid operator")

except Exception as e:
    print("invalid input!!! reason is : ", e)