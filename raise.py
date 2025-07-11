#raise[exception[,args[,traceback]]]
try:
    num=11
    print(num)
    raise ValueError
except:
    print("Exception Occured")

#traceback (most recent calls)