try:
    print("Raising Exception")
    raise ValueError
except:
    print("Exception caught...........")
finally:
    print("performing clean-up in finally")