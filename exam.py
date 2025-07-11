n=int(input("enter the n valu:"))
with open("File.txt","r") as f:
    res=f.readlines()
for r in res[:n]:
    print(r.strip())