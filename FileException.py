try:
    file=open("File.txt")
    str=file.readline()
    print(str)
    file=open("File.txt")
    str=file.readline()
    print(str)
except IOError:
    print("Error occured during input take......")
else:
    print("successfully fetch the data........")