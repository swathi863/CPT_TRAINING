import sys
'''
print("Script name:",sys.argv[0])
print("All args:",sys.argv[1:])
print("Number of items:",len(sys.argv))
print("Including file name:",sys.argv)
if len(sys.argv)>1:
	print("Frist arg :",sys.argv[1])
else:
	print("No args provided")
'''
#product
'''
num1=int(sys.argv[1])
num2=int(sys.argv[2])
num3=int(sys.argv[3])
print("Sum:",num1+num2)
print("Product:",num1*num2*num3)

'''
'''
if len(sys.argv)!=3:
	print("Usage: python arguments1.py l b")
else:
	l=float(sys.argv[1])
	b=float(sys.argv[2])
	print("Calcuulated area:",l*b)
'''	
'''
if len(sys.argv)<2:
	print("Usage : python sample.py n1,n2,....")
	sys.exit()
numbers=[int(arg) for arg in sys.argv[1:]]
total=sum(numbers)
print("Numbers:",numbers)
print("Sum:",total)

'''
import argparse
'''
parser=argparse.ArgumentParser(description="Add 2 Numbers")
parser.add_argument('--x',type=int,required=True,help="Frist Number")
parser.add_argument('--y',type=int,required=True,help="Second Number")
args=parser.parse_args()
result=args.x+args.y
print("Sum is ",result)
'''
#calc evaluation using parse
'''
parser=argparse.ArgumentParser(description="Simple Calcluator")
parser.add_argument('--x',type=int,required=True,help="Frist Number")
parser.add_argument('--y',type=int,required=True,help="Second Number")
parser.add_argument('--opt',type=str,required=True,choices=['add','sub','mul','div'], help="Operation")
args=parser.parse_args()
if args.opt=='add':
	result=args.x+args.y
elif args.opt=='mul':
	result=args.x*args.y
elif args.opt=='sub':
	result=args.x-args.y
elif args.opt=='div':
	result=args.x/args.y

print("	Result is: ",result)
'''
#checking the files using path
import os 
'''
path="."
files=os.listdir(path)
print("Files and folders in current dirextory:")
for f in files:
	print(f)
'''
#creating a floder
'''
folder = "new_Folder"
if not os.path.exists(folder):
	os.mkdir(folder)
	print(f" folder '{folder}' created.")
else:
	print(f"Folder '{folder}' already exists.")
'''
#deleting a file 
'''
file="Deleteme.txt"
if os.path.exists(file):
	os.remove(file)
	print(f"{file} delete")
else:
	print("file not found")
'''
#getting size of a particular file
'''
file="arguments1.py"
if os.path.exists(file):
	size=os.path.getsize(file)
	print(f"{file} size:{size} bytes.")
else:
	print("file not found")
'''












