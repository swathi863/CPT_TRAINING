import json
name=input("enter the name: ")
age=int(input("enter age:"))
user={"name":name,"age":age}
with open("user.json","w") as f:#f means file
    json.dump(user,f)#dump the data from the outside page
print("Data Written to Json Floder")
with open("user.json",'r') as f:
    loaded=json.load(f) #retriving the data from the json
    print("read from file",loaded)