#!/usr/bin/env python
# coding: utf-8

# In[1]:


class fun():
    var=100
    def display(self):
        print("This is class method")
obj = fun()
print(obj.var)
obj.display()


# In[2]:


#class constructer __init__ (method)
class fun():
    def __init__(self , val):
        print("This is class method")
        self.val=val
        print("the value:",val)
obj=fun(10)


# In[3]:


class abc():
    cv=0
    def __init__(self,var):
        abc.cv+=1
        self.var=var
        print("object var:",var)
        print("class var:",abc.cv)
obj=abc(10)
obj=abc(20)


# In[4]:


class abc(): 
    def __init__(self,n):
        if n%2==0:
            print(n,"is even")
        else:
            print("odd")
obj=abc(6)


# In[5]:


class number:
    even=0
    def check(self,num):
        if num%2==0:
            self.even=1
    def eo(self,num):
        self.check(num)
        if self.even ==1:
            print(num,"is even")
        else:
            print(num,"is odd")
n=number()
n.eo(24)


# In[6]:


class number:
    even=[]
    odd=[]
    def __init__(self,num):
        self.num=num
        if num%2==0:
            number.even.append(num)
        else:
            number.odd.append(num)
n1=number(21)
n2=number(32)
n3=number(43)
n4=number(54)
n5=number(65)
print("even numbers:",number.even)
print("odd numbers :",number.odd)


# In[7]:


class number:
    even=[]
    odd=[]
    def __init__(self,num):
        self.num=num
        if num%2==0:
            number.even.append(num)
        else:
            number.odd.append(num)
n1=number(21)
n2=number(32)
n3=number(43)
n4=number(54)
n5=number(65)
print("even numbers:",number.even)
print("odd numbers :",number.odd)


# In[8]:


class abc():
    def __init__(self,name,var):
        self.name=name
        self.var=var
    def __repr__(self):
        return repr(self.var)
    def __len__(self):
        return len(self.name)
    def __cmp__(self,obj):
        return self.var-obj.var
obj = abc("pujitha",20)
print("the value stored in object is :",repr(obj))
print("the length of name stored in object:",len(obj))
obj1=abc("jaswanth",1)
val=obj.__cmp__(obj1)
if val==0:
    print("both the values are equal")
elif val==-1:
    print("first value is less then second")
else:
    print("second value is less than first")


# In[9]:


class numbers:
    def __init__(self,mylist):
        self.mylist=mylist
    def __getitem__(self,index):
        return self.mylist[index]
    def __setitem__(self,index,val):
        self.mylist[index]=val
numlist=numbers([1,2,3,4,5,6,7,8,9])
print(numlist)
numlist[3]=10
print(numlist.mylist)


# In[ ]:




