import csv 
with open("people.csv","w",newline="") as file:
    writer=csv.writer(file)
    writer.writerow(["name","age"])
    for _ in range(2):#"_" this is used for taking empty bucket in for loop
        name=input("enter name:")
        age=input("Enter age:")
        writer.writerow([name,age])#write the datain the csv file
print("Data written on csv file")