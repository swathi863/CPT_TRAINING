'''with open("File1.txt","r+") as file:
    file.write("Wipro,TCS,Capgemini")
'''
'''
with open("File1.txt","r+") as file:
    content=file.read()
    #print(content)
    file.seek(0)
    file.write("modified done here")
'''
'''
with open("File1.txt",'a+') as file:
    file.write('\n Append data')
    file.seek(0)
    print(file.read())
'''
'''
with open('File1.txt','r') as f:
    lines=f.readlines()
print("List of lines:",lines)

with open('File1.txt','r') as f:
    lines=f.readlines()
for i in lines:
    print("List of lines:",i.strip())
'''
'''
with open('File1.txt','r') as f:
    seprate_lines=[line.strip() for line in f.readlines()]
    print(seprate_lines)
close()-manually
'''
'''
file=open('File1.txt','r')
print(file.closed)
file.close()
print(file.closed)
'''
"""program to create a txt file access the text file data and use the   data to split the 
line into series of words and use space to perform split operation
sample.txt
Hello Students 
How are you today
output:
['Hello','students','how','are','you','today']
"""
'''
with open("sample.txt",'r') as f:
    l=[j.strip() for i in f.readlines() for j in i.split(" ")]
    print(l)
'''
with open("sample.txt",'r') as f1,open('file1.txt','r') as f2:
    c1=f1.read()
    c2=f2.read()
    print("data in file 1:")
    print(c1)
    print("data in file2")
    print(c2)    
    f1.close()
    f2.close()