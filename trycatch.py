num=int(input("Enter the numerator:"))
dem=int(input("Enter the denomerator:"))
try:
    quo=num/dem
    print("Quotient:",quo)
except ZeroDivisionError:
    print("Denominator can't be zero")