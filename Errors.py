#OverFlow error
'''
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(10000))
'''
'''
import math
# Example computation involving large numbers
result = math.exp(1000)
print(result)
'''
#FloatingpointError
'''
decimal_number = 0.1
binary_representation = format(decimal_number, '.30f')  # 30 decimal places
print(f"Decimal: {decimal_number}\nBinary: {binary_representation}")
'''
#keyerror
'''
# Creating a Dictionary
subjects = {'Sree': 'Maths',
            'Ram': 'Biology',
            'Shyam': 'Science',
            'Abdul': 'Hindi'}

# Printing the subject of Fharan
print(subjects['Fharan'])
'''
#OSError
# Importing os module
'''
import os

# os.ttyname() method in Python is used to get the terminal 
# device associated with the specified file descriptor.
# and raises an exception if the specified file descriptor 
# is not associated with any terminal device.
print(os.ttyname(1))
'''
#ModuleNotFoundError
'''
try:
    import module_name
except ModuleNotFoundError:
    print("The module 'module_name' is not installed. ")
    # You can include additional instruction here, such as installing the module.
else:
    # Code to run if the module  is successfully imported
    print(" Module 'module_name' is installed. ")
'''
